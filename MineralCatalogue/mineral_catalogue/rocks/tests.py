from django.test import TestCase
from .models import Mineral
from django.utils import timezone


# Create your tests here.


class Test_Mineral_Model(TestCase):

    def test_model_creation(self):
        a = Mineral.objects.create(name="daa",
                                  image_filename="kasma",
                                  image_caption="ansdkq",
                                  category="kdCJXA",
                                  formula="wDNA",
                                  strunz_classification="KCDAX",
                                  color="",
                                  crystal_system="",
                                  unit_cell="",
                                  crystal_symmetry="",
                                  cleavage="",
                                  mohs_scale_hardness="",
                                  luster="",
                                  streak="",
                                  diaphaneity="",
                                  optical_properties="",
                                  refractive_index="",
                                  crystal_habit="",
                                  specific_gravity="")


        self.assertTrue(a.name)
