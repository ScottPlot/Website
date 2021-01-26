// Angle and Magnitude
// This example demonstrates how to define vectors according to a given angle and magnitude.
var plt = new ScottPlot.Plot(600, 400);

double[] xs = DataGen.Range(-5, 6);
double[] ys = DataGen.Range(-5, 6);
Vector2[,] vectors = new Vector2[xs.Length, ys.Length];

for (int i = 0; i < xs.Length; i++)
{
    for (int j = 0; j < ys.Length; j++)
    {
        double slope = -xs[i];
        double magnitude = Math.Abs(xs[i]);
        double angle = Math.Atan(slope);

        vectors[i, j] = new Vector2(Math.Cos(angle) * magnitude, Math.Sin(angle) * magnitude);
    }
}

plt.AddVectorField(vectors, xs, ys);

plt.SaveFig("vectorField_angleMag.png");