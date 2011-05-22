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

from django.core.exceptions import ValidationError
from django.test import TestCase

from promotions.models import Promotion, PromotionName


class PromotionNameTest(TestCase):

    def setUp(self):
        self.p1 = Promotion.objects.create(start_date="2000-02-01",
                                           end_date="2000-03-01")
        self.p2 = Promotion.objects.create(start_date="2000-02-01")

    def assertRaisesValidationError(self, promotion, name, start_date,
                                    end_date=None):
        self.assertRaises(ValidationError,
                          PromotionName.objects.create,
                          obj=promotion,
                          start_date=start_date,
                          end_date=end_date,
                          name=name)

    def test_not_older_than_promotion(self):
        self.assertRaisesValidationError(self.p1, "Pre Name", "2000-01-01")
        self.assertRaisesValidationError(self.p2, "Pre Name", "2000-01-01")

    def test_not_newer_than_promotion(self):
        self.assertRaisesValidationError(self.p1, "Post Name", "2000-04-01")

    def test_doesnt_end_after_promotion(self):
        self.assertRaisesValidationError(self.p1, "After Name", "2000-02-01",
                                         "2000-04-01")

    def test_start_before_end(self):
        self.assertRaisesValidationError(self.p1, "After Name", "2000-04-01",
                                         "2000-02-01")
        self.assertRaisesValidationError(self.p2, "After Name", "2000-04-01",
                                         "2000-02-01")

    def test_only_one_latest(self):
        PromotionName.objects.create(obj=self.p2, start_date="2000-02-01",
                                     name="Foo")
        self.assertRaisesValidationError(self.p2, "Bar", "2000-04-01")

    def test_promotion_name(self):
        self.assertRaises(PromotionName.DoesNotExist, self.p2.name)
        n1 = PromotionName.objects.create(obj=self.p2, name="A",
                                          start_date="2000-02-01")
        self.assertEqual("A", self.p2.name())
        n1.end_date = "2000-03-01"
        n1.save()
        self.assertEqual("A", self.p2.name())
        n2 = PromotionName.objects.create(obj=self.p2, name="B",
                                          start_date="2000-03-01")
        self.assertEqual("B", self.p2.name())
