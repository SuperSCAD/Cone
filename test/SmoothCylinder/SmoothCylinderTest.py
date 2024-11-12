from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad_smooth_profiles.FilletFactory import FilletFactory

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
                                  top_inner_profile=FilletFactory(radius=3.0),
                                  top_outer_profile=FilletFactory(radius=3.0),
                                  bottom_outer_profile=FilletFactory(radius=3.0),
                                  bottom_inner_profile=FilletFactory(radius=3.0),
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

# ----------------------------------------------------------------------------------------------------------------------
