from django.test import TestCase
from .models import Mineral
from django.utils import timezone


# Create your tests here.


class Test_Mineral_Model(TestCase):

    def test_model_creation(self):
        self.a = Mineral.objects.create(name="daa",
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


        self.assertTrue(self.a)

    def test_two_instances_are_same(self):
        self.a = Mineral.objects.create(name="daa",
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

        self.b = Mineral.objects.create(name="daa",
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



        self.assertNotEqual(self.a,self.b)


class Test_views(TestCase):

    def setUp(self):
        self.a = Mineral.objects.create(name="daa",
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

        self.b = Mineral.objects.create(name="daa",
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

