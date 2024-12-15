from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad_smooth_profiles.Chamfer import Chamfer
from super_scad_smooth_profiles.Fillet import Fillet

from super_scad_cone.SmoothCone import SmoothCone
from test.ScadTestCase import ScadTestCase


class SmoothConeTest(ScadTestCase):
    """
    Testcases for smooth cones.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_smooth_cone(self) -> None:
        """
        Test with a plain smooth cone.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=60, eps=0.1))
        cone = SmoothCone(height=50.0,
                          top_outer_diameter=25.0,
                          top_inner_diameter=10.0,
                          bottom_outer_diameter=35.0,
                          bottom_inner_diameter=10.0,
                          top_inner_profile=Fillet(radius=3.0),
                          top_outer_profile=Fillet(radius=4.0),
                          bottom_outer_profile=Chamfer(skew_length=5.0),
                          bottom_inner_profile=Chamfer(skew_length=5.0),
                          rotate_extrude_angle=180.0)

        self.assertAlmostEqual(50.0, cone.height)
        self.assertAlmostEqual(12.5, cone.top_outer_radius)
        self.assertAlmostEqual(25.0, cone.top_outer_diameter)
        self.assertAlmostEqual(5.0, cone.top_inner_radius)
        self.assertAlmostEqual(10.0, cone.top_inner_diameter)
        self.assertAlmostEqual(17.5, cone.bottom_outer_radius)
        self.assertAlmostEqual(35.0, cone.bottom_outer_diameter)
        self.assertAlmostEqual(5.0, cone.bottom_inner_radius)
        self.assertAlmostEqual(10.0, cone.bottom_inner_diameter)
        self.assertFalse(cone.top_extend_by_eps)
        self.assertFalse(cone.bottom_extend_by_eps)
        self.assertFalse(cone.center)
        self.assertAlmostEqual(180.0, cone.rotate_extrude_angle)
        self.assertEqual(2, cone.convexity)

        scad.run_super_scad(cone, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_extend_by_eps(self) -> None:
        """
        Test with a plain smooth cone.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=60, eps=0.1))
        cone = SmoothCone(height=10.0,
                          top_outer_diameter=25.0,
                          top_inner_diameter=10.0,
                          bottom_outer_diameter=35.0,
                          bottom_inner_diameter=10.0,
                          top_inner_profile=Fillet(radius=2.0),
                          top_outer_profile=Fillet(radius=2.0),
                          bottom_outer_profile=Chamfer(skew_length=2.0),
                          bottom_inner_profile=Chamfer(skew_length=2.0),
                          top_extend_by_eps=True,
                          bottom_extend_by_eps=True,
                          rotate_extrude_angle=180.0)
        self.assertTrue(cone.top_extend_by_eps)
        self.assertTrue(cone.bottom_extend_by_eps)

        scad.run_super_scad(cone, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
