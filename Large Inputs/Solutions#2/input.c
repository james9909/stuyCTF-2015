#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define NUMBER_OF_RANDOMS 23

double reverseAlgorithm(long input, double *numbers, int length_numbers);
double formula(double x, double c, double d);
long algorithm(long input, double *numbers, int length_numbers);

double numbers[] = {3570793128, 1458104314, 3260858022, 1345134392, 749597442, 289067508, 2759917644, 181602112, 1449980724, 1535408668, 988033496, 1457695096, 1802710596, 2496283884, 34647282, 2272064548, 3969791992, 2236522198, 2371091990, 3947054260, 338067104, 4274799248, 101450696};

double reverseAlgorithm(long input, double *numbers, int length_numbers) {
	double result = input;
	int i;
	for (i = 22; i >= 1; --i) {
		result = formula(result, numbers[i], numbers[i-1]);
		printf("%lf\n" , result);
	}
	printf("\n");
	return result; 
}

double formula(double x, double c, double d) {
	double product = c * x;
	double squareR = sqrt( (pow(product, 2)) - (4 * d * c) );
	
	// ROOTS
	double positiveR = .5 * (product + squareR);
	double negativeR = .5 * (product - squareR);
	
	if (positiveR > negativeR) {
		return positiveR;
	} else {
		return negativeR;
	}
}

int main() {
	long computer = 5362426;
	printf("\n%lf\n", reverseAlgorithm(computer, numbers, NUMBER_OF_RANDOMS));
	//printf("\n%lu\n", algorithm((long) reverseAlgorithm(computer, numbers, NUMBER_OF_RANDOMS), numbers, 23));
}