# moore - a wrestling database
# Copyright (C) 2011  Daniel Watkins
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from matches.models import Card, Match
from wrestlers.models import Wrestler


class MatchTestCase(TestCase):

    fixtures = ['test.json']

    def setUp(self):
        self.card = Card.objects.get(id=1)
        self.w1 = Wrestler.objects.get(id=1)
        self.w2 = Wrestler.objects.get(id=2)
        self.w3 = Wrestler.objects.get(id=3)

    def _create_two_person_match(self, order_num=None):
        m = Match(card=self.card)
        if order_num is not None:
            m.order = order_num
        m.save()
        m.add_competitor(self.w1)
        m.add_competitor(self.w2)
        m.save()
        return m


class MatchTest(MatchTestCase):

    def test_vs_string(self):
        """
        Tests that the vs. string works for different numbers of
        wrestlers.
        """
        m = self._create_two_person_match()
        self.assertEqual("%s vs. %s" % (self.w1.name, self.w2.name),
                         m.vs_string())
        m.add_competitor(self.w3)
        m.save()
        self.assertEqual("%s vs. %s vs. %s" % (self.w1.name,
                                               self.w2.name,
                                               self.w3.name),
                         m.vs_string())

    def test_unicode(self):
        m = self._create_two_person_match()
        self.assertEqual("%s: %s" % (self.card.date, m.vs_string()),
                         unicode(m))
        m.add_competitor(self.w3)
        m.save()
        self.assertEqual("%s: %s" % (self.card.date, m.vs_string()),
                         unicode(m))

    def test_winner_in_match(self):
        m = self._create_two_person_match()
        m.winner = self.w3
        m.save()
        self.assertEqual(0, len(Match.objects.filter(winner=self.w3)))


class TestReview(MatchTestCase):

    def test_update_time(self):
        before = datetime.now()
        m = self._create_two_person_match()
        after = datetime.now()
        self.assertTrue(before < m.updated_at < after)

    def test_update_time_changed_on_m2m(self):
        m = self._create_two_person_match()
        before_time = m.updated_at
        m.add_competitor(self.w3)
        self.assertTrue(before_time < m.updated_at)

    def test_reviewed(self):
        m = self._create_two_person_match()
        self.assertFalse(m.reviewed)
        m.reviewed_by = User.objects.get(id=1)
        m.save()
        self.assertTrue(m.reviewed, "%s != %s" % (m.reviewed_at, m.updated_at))
        m.add_competitor(self.w3)
        self.assertFalse(m.reviewed)


class CaseTest(MatchTestCase):

    def test_explicit_next_order_number(self):
        # With no matches, the next order number should be 1
        self.assertEqual(1, self.card.next_order_number())
        # Multiple calls with no new matches should be the same
        self.assertEqual(1, self.card.next_order_number())

        self._create_two_person_match(order_num=1)
        self.assertEqual(2, self.card.next_order_number())

        self._create_two_person_match(order_num=3)
        self.assertEqual(2, self.card.next_order_number())

        self._create_two_person_match(order_num=2)
        self.assertEqual(4, self.card.next_order_number())

    def test_implicit_next_order_number(self):
        self.assertEqual(1, self.card.next_order_number())
        self._create_two_person_match()
        self.assertEqual(2, self.card.next_order_number())
        self._create_two_person_match(order_num=3)
        self.assertEqual(2, self.card.next_order_number())
        self._create_two_person_match()
        self.assertEqual(4, self.card.next_order_number())
