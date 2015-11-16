#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUMBER_OF_RANDOMS 23

double numbers[] = {3570793128, 1458104314, 3260858022, 1345134392, 749597442, 289067508, 2759917644, 181602112, 1449980724, 1535408668, 988033496, 1457695096, 1802710596, 2496283884, 34647282, 2272064548, 3969791992, 2236522198, 2371091990, 3947054260, 338067104, 4274799248, 101450696};
double answers[1000];
int answers_index = 0;

// y = x / n + m / x
// Where y = new result
//       x = old result
//       n = numbers[i]
//       m = numbers[i-1]
long algorithm(long input, double *numbers, int length_numbers) {
    double result = input;
    int i;
    for (i=1; i<length_numbers; ++i) {
        result = (result / numbers[i] + numbers[i-1] / result);
    }
    return (long) result;
}

// Reversal of the above algorithm using
// x^2 - nyx + mn = 0
void reverseAlgorithm(double result, double *numbers, int index) {
    double *roots = (double *) malloc(2 * sizeof(double));
    if (index >= 1) {
        double a = 1;
        double b = -result * numbers[index];
        double c = numbers[index] * numbers[index-1];

        // Two possible roots
        roots[0] = (-b + sqrt(b*b - 4*a*c)) / (2*a);
        roots[1] = (-b - sqrt(b*b - 4*a*c)) / (2*a);

        reverseAlgorithm(roots[0], numbers, index - 1);
        reverseAlgorithm(roots[1], numbers, index - 1);
    }
    else {
        // Ignore mad weird answers
        if (!isnan(result) && !isinf(result)) {
            answers[answers_index] = result;
            answers_index++;
        }
    }
}

int main() {
    long input;
    long computer = 5362426;

    reverseAlgorithm(computer, numbers, 22);

    int i;
    for (i = 0; i < sizeof(answers); i++) {
        double ans = answers[i];
        if (ans > 0) {
            printf("%lf \n", answers[i]);
        }
    }
}
