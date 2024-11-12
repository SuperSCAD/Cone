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
               polygon(points = [[5.0, 20.0], [12.5, 20.0], [12.5, 0.0], [12.5, 0.0], [9.5, 0.0], [9.5, -0.1], [8.0, -0.1], [8.0, 0.0], [5.0, 0.0]], convexity = 2);
               translate(v = [5.0, 20.0])
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
            translate(v = [12.5, 20.0])
            {
               rotate(a = 315.0)
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
         translate(v = [12.5, 0.0])
         {
            rotate(a = 225.0)
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
      translate(v = [5.0, 0.0])
      {
         rotate(a = 135.0)
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
}
