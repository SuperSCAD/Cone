// Unit of length: Unit.MM
$fn = 60;

rotate_extrude(angle = 180.0, convexity = 2)
{
   union()
   {
      difference()
      {
         polygon(points = [[5.0, 10.0], [5.0, 10.0], [7.0, 10.0], [7.0, 10.1], [11.2639, 10.1], [11.2639, 10.0], [12.5, 10.0], [17.5, 0.0], [17.5, 0.0], [15.5979, 0.0], [15.5979, -0.1], [6.4142, -0.1], [6.4142, 0.0], [5.0, 0.0]], convexity = 2);
         translate(v = [5.0, 10.0])
         {
            rotate(a = 45.0)
            {
               difference()
               {
                  polygon(points = [[0.0, 0.1414], [1.4849, -1.3435], [1.4142, -1.4142], [-1.4142, -1.4142], [-1.4849, -1.3435]], convexity = 2);
                  translate(v = [0.0, -2.8284])
                  {
                     circle(d = 4.0, $fn = 60);
                  }
               }
            }
         }
         translate(v = [12.5, 10.0])
         {
            rotate(a = 328.2825)
            {
               difference()
               {
                  polygon(points = [[0.0, 0.1176], [1.104, -0.5648], [1.0515, -0.6498], [-1.0515, -0.6498], [-1.104, -0.5648]], convexity = 2);
                  translate(v = [0.0, -2.3511])
                  {
                     circle(d = 4.0, $fn = 60);
                  }
               }
            }
         }
         polygon(points = [[17.5894, 0.0447], [17.5851, -0.0526], [17.5, -0.1], [15.5979, -0.1], [15.5979, 0.0], [16.6493, 1.7013], [16.7388, 1.746]]);
         polygon(points = [[4.9, -0.1], [4.9, 1.4142], [5.0, 1.4142], [6.4142, 0.0], [6.4142, -0.1]]);
      }
   }
}
