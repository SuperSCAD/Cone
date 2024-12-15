// Unit of length: Unit.MM
$fn = 60;

rotate_extrude(angle = 360.0)
{
   union()
   {
      difference()
      {
         polygon(points = [[0.0, 50.0], [2.5, 50.0], [2.5, 0.0], [0.0, 0.0]]);
      }
   }
}
