// Unit of length: Unit.MM
$fn = 60;

union()
{
   difference()
   {
      cube(size = [100.0, 50.0, 15.0], center = false);
      translate(v = [20.0, 25.0, 0.0])
      {
         rotate_extrude(angle = 360.0)
         {
            union()
            {
               difference()
               {
                  polygon(points = [[0.0, 15.0], [0.0, 15.01], [5.0, 15.01], [5.0, 15.0], [5.0, 0.0], [5.0, -0.01], [0.0, -0.01], [0.0, 0.0]]);
               }
               translate(v = [5.0, 15.0])
               {
                  polygon(points = [[-0.01, 0.01], [2.8284, 0.01], [2.8284, 0.0], [0.0, -2.8284], [-0.01, -2.8284]]);
               }
            }
         }
      }
      translate(v = [40.0, 25.0, 0.0])
      {
         rotate_extrude(angle = 360.0)
         {
            union()
            {
               difference()
               {
                  polygon(points = [[0.0, 15.0], [0.0, 15.01], [5.0, 15.01], [5.0, 15.0], [5.0, 0.0], [5.0, -0.01], [0.0, -0.01], [0.0, 0.0]]);
               }
               translate(v = [5.0, 15.0])
               {
                  polygon(points = [[-0.01, 0.01], [2.8284, 0.01], [2.8284, 0.0], [0.0, -2.8284], [-0.01, -2.8284]]);
               }
            }
         }
      }
      translate(v = [60.0, 25.0, 0.0])
      {
         rotate_extrude(angle = 360.0)
         {
            union()
            {
               difference()
               {
                  polygon(points = [[0.0, 15.0], [0.0, 15.01], [5.0, 15.01], [5.0, 15.0], [5.0, 0.0], [5.0, -0.01], [0.0, -0.01], [0.0, 0.0]]);
               }
               translate(v = [5.0, 15.0])
               {
                  polygon(points = [[-0.01, 0.01], [2.8284, 0.01], [2.8284, 0.0], [0.0, -2.8284], [-0.01, -2.8284]]);
               }
            }
         }
      }
      translate(v = [80.0, 25.0, 0.0])
      {
         rotate_extrude(angle = 360.0)
         {
            union()
            {
               difference()
               {
                  polygon(points = [[0.0, 15.0], [0.0, 15.01], [5.0, 15.01], [5.0, 15.0], [5.0, 0.0], [5.0, -0.01], [0.0, -0.01], [0.0, 0.0]]);
               }
               translate(v = [5.0, 15.0])
               {
                  polygon(points = [[-0.01, 0.01], [2.8284, 0.01], [2.8284, 0.0], [0.0, -2.8284], [-0.01, -2.8284]]);
               }
            }
         }
      }
   }
   translate(v = [60.0, 25.0, 16.0])
   {
      color(c = [1.0, 0.0, 0.0, 1.0])
      {
         rotate_extrude(angle = 360.0)
         {
            union()
            {
               difference()
               {
                  polygon(points = [[0.0, 15.0], [0.0, 15.01], [5.0, 15.01], [5.0, 15.0], [5.0, 0.0], [5.0, -0.01], [0.0, -0.01], [0.0, 0.0]]);
               }
               translate(v = [5.0, 15.0])
               {
                  polygon(points = [[-0.01, 0.01], [2.8284, 0.01], [2.8284, 0.0], [0.0, -2.8284], [-0.01, -2.8284]]);
               }
            }
         }
      }
   }
}
