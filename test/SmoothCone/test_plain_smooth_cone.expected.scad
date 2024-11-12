// Unit of length: Unit.MM
$fa = 1.0;
$fs = 0.1;

rotate_extrude(angle = 180.0, convexity = 2)
{
   difference()
   {
      difference()
      {
         difference()
         {
            difference()
            {
               polygon(points = [[5.0, 50.0], [12.5, 50.0], [17.5, 0.0], [5.0, 0.0]], convexity = 2);
               translate(v = [5.0, 50.0])
               {
                  rotate(a = 45.0)
                  {
                     difference()
                     {
                        polygon(points = [[0.0, 0.1414], [2.192, -2.0506], [2.1213, -2.1213], [-2.1213, -2.1213], [-2.192, -2.0506]], convexity = 2);
                        translate(v = [0.0, -4.2426])
                        {
                           circle(d = 6.0, $fn = 192);
                        }
                     }
                  }
               }
            }
            translate(v = [12.5, 50.0])
            {
               rotate(a = 317.8553)
               {
                  difference()
                  {
                     polygon(points = [[0.0, 0.1349], [2.7511, -2.3549], [2.684, -2.429], [-2.684, -2.429], [-2.7511, -2.3549]], convexity = 2);
                     translate(v = [0.0, -5.3948])
                     {
                        circle(d = 8.0, $fn = 252);
                     }
                  }
               }
            }
         }
         polygon(points = [[17.5995, 0.01], [17.5741, -0.0671], [17.5, -0.1], [13.7742, -0.1], [13.7742, 0.0], [17.1293, 3.7073], [17.2288, 3.7172]]);
      }
      polygon(points = [[4.9, -0.1], [4.9, 3.5355], [5.0, 3.5355], [8.5355, 0.0], [8.5355, -0.1]]);
   }
}
