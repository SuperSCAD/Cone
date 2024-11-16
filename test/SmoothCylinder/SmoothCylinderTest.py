from super_scad.boolean.Compound import Compound
from super_scad.boolean.Difference import Difference
from super_scad.d3.Cuboid import Cuboid
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.transformation.Paint import Paint
from super_scad.transformation.Translate3D import Translate3D
from super_scad.type.Color import Color
from super_scad_smooth_profiles.ExteriorChamferFactory import ExteriorChamferFactory
from super_scad_smooth_profiles.InteriorFilletFactory import InteriorFilletFactory

from super_scad_cone.SmoothCylinder import SmoothCylinder
from test.ScadTestCase import ScadTestCase


class SmoothCylinderTest(ScadTestCase):
    """
    Testcases for smooth cylinders.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_cylinder(self) -> None:
        """
        Test with a plain cylinder.
        """
        scad = Scad(context=Context(fs=0.1, fa=1.0, eps=0.1))
        cylinder = SmoothCylinder(height=50.0, diameter=5.0)

        self.assertAlmostEqual(50.0, cylinder.height)
        self.assertAlmostEqual(2.5, cylinder.outer_radius)
        self.assertAlmostEqual(5.0, cylinder.outer_diameter)
        self.assertAlmostEqual(0.0, cylinder.inner_radius)
        self.assertAlmostEqual(0.0, cylinder.inner_diameter)
        self.assertFalse(cylinder.top_extend_by_eps)
        self.assertFalse(cylinder.bottom_extend_by_eps)
        self.assertFalse(cylinder.center)
        self.assertIsNone(cylinder.convexity)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(cylinder, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_hollow_smooth_cylinder(self) -> None:
        """
        Test with a plain cylinder.
        """
        scad = Scad(context=Context(fs=0.1, fa=1.0, eps=0.1))
        cylinder = SmoothCylinder(height=20.0,
                                  outer_diameter=25.0,
                                  inner_diameter=10.0,
                                  top_inner_profile=InteriorFilletFactory(radius=3.0),
                                  top_outer_profile=InteriorFilletFactory(radius=3.0),
                                  bottom_outer_profile=InteriorFilletFactory(radius=3.0),
                                  bottom_inner_profile=InteriorFilletFactory(radius=3.0),
                                  bottom_extend_by_eps=True,
                                  rotate_extrude_angle=180.0)

        self.assertAlmostEqual(20.0, cylinder.height)
        self.assertAlmostEqual(12.5, cylinder.outer_radius)
        self.assertAlmostEqual(25.0, cylinder.outer_diameter)
        self.assertAlmostEqual(5.0, cylinder.inner_radius)
        self.assertAlmostEqual(10.0, cylinder.inner_diameter)
        self.assertFalse(cylinder.top_extend_by_eps)
        self.assertTrue(cylinder.bottom_extend_by_eps)
        self.assertFalse(cylinder.center)
        self.assertEqual(2, cylinder.convexity)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(cylinder, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_punch(self) -> None:
        """
        Test with creating a hole in a punch.
        """
        scad = Scad(context=Context(fs=0.1, fa=1.0))

        thickness = 15.0
        material = Cuboid(width=100.0, depth=50.0, height=thickness)

        punch = SmoothCylinder(height=thickness,
                               diameter=10.0,
                               top_outer_profile=ExteriorChamferFactory(skew_height=2.0, side=2),
                               top_extend_by_eps=True,
                               bottom_extend_by_eps=True)

        material = Difference(children=[material,
                                        Translate3D(x=20, y=25, child=punch),
                                        Translate3D(x=40, y=25, child=punch),
                                        Translate3D(x=60, y=25, child=punch),
                                        Translate3D(x=80, y=25, child=punch)])

        composition = Compound(children=[material,
                                         Translate3D(x=60,
                                                     y=25,
                                                     z=thickness + 1.0,
                                                     child=Paint(color=Color('red'), child=punch))])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(composition, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
