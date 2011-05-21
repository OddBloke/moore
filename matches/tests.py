"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from matches.models import Card, Match
from wrestlers.models import Wrestler


class MatchTest(TestCase):

    fixtures = ['test.json']

    def setUp(self):
        self.card = Card.objects.get(id=1)
        self.w1 = Wrestler.objects.get(id=1)
        self.w2 = Wrestler.objects.get(id=2)
        self.w3 = Wrestler.objects.get(id=3)

    def _create_two_person_match(self):
        m = Match.objects.create(card=self.card)
        m.save()
        m.participants.add(self.w1)
        m.participants.add(self.w2)
        m.save()
        return m

    def test_vs_string(self):
        """
        Tests that the vs. string works for different numbers of
        wrestlers.
        """
        m = self._create_two_person_match()
        self.assertEqual("%s vs. %s" % (self.w1.name, self.w2.name),
                         m.vs_string())
        m.participants.add(self.w3)
        m.save()
        self.assertEqual("%s vs. %s vs. %s" % (self.w1.name,
                                               self.w2.name,
                                               self.w3.name),
                         m.vs_string())

    def test_unicode(self):
        m = self._create_two_person_match()
        self.assertEqual("%s: %s" % (self.card.date, m.vs_string()),
                         unicode(m))
        m.participants.add(self.w3)
        m.save()
        self.assertEqual("%s: %s" % (self.card.date, m.vs_string()),
                         unicode(m))
