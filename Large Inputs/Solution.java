import java.math.*;

public class Solution {
    static BigInteger numbers[] = {BigInteger.valueOf(3570793128L),
        BigInteger.valueOf(1458104314L),
        BigInteger.valueOf(3260858022L),
        BigInteger.valueOf(1345134392),
        BigInteger.valueOf(749597442),
        BigInteger.valueOf(289067508),
        BigInteger.valueOf(2759917644L),
        BigInteger.valueOf(181602112),
        BigInteger.valueOf(1449980724),
        BigInteger.valueOf(1535408668L),
        BigInteger.valueOf(988033496),
        BigInteger.valueOf(1457695096),
        BigInteger.valueOf(1802710596),
        BigInteger.valueOf(2496283884L),
        BigInteger.valueOf(34647282),
        BigInteger.valueOf(2272064548L),
        BigInteger.valueOf(3969791992L),
        BigInteger.valueOf(2236522198L),
        BigInteger.valueOf(2371091990L),
        BigInteger.valueOf(3947054260L),
        BigInteger.valueOf(338067104),
        BigInteger.valueOf(4274799248L),
        BigInteger.valueOf(101450696)};

    public static BigInteger bigIntSqRootCeil(BigInteger x)
        throws IllegalArgumentException {
        if (x.compareTo(BigInteger.ZERO) < 0) {
            throw new IllegalArgumentException("Negative argument.");
        }
        // square roots of 0 and 1 are trivial and
        // y == 0 will cause a divide-by-zero exception
        if (x == BigInteger.ZERO || x == BigInteger.ONE) {
            return x;
        } // end if
        BigInteger two = BigInteger.valueOf(2L);
        BigInteger y;
        // starting with y = x / 2 avoids magnitude issues with x squared
        for (y = x.divide(two);
                y.compareTo(x.divide(y)) > 0;
                y = ((x.divide(y)).add(y)).divide(two));
        if (x.compareTo(y.multiply(y)) == 0) {
            return y;
        } else {
            return y.add(BigInteger.ONE);
        }
    }

    public static BigInteger bigIntSqRootFloor(BigInteger x)
            throws IllegalArgumentException {
        if (x.compareTo(BigInteger.ZERO) < 0) {
            throw new IllegalArgumentException("Negative argument.");
        }
        // square roots of 0 and 1 are trivial and
        // y == 0 will cause a divide-by-zero exception
        if (x .equals(BigInteger.ZERO) || x.equals(BigInteger.ONE)) {
            return x;
        } // end if
        BigInteger two = BigInteger.valueOf(2L);
        BigInteger y;
        // starting with y = x / 2 avoids magnitude issues with x squared
        for (y = x.divide(two);
                y.compareTo(x.divide(y)) > 0;
                y = ((x.divide(y)).add(y)).divide(two));
        return y;
    } // end bigIntSqRootFloor

    public static void revAlgorithm(long input) {
        BigInteger two = BigInteger.valueOf(2);
        BigInteger result = BigInteger.valueOf(input);
        BigInteger resultAlt = BigInteger.valueOf(input);
        // Reversed for loop i values
        for (int i = 22; i > 0; i--) {
            // Current algorithm, doesnt work
            BigInteger nm = numbers[i].multiply(numbers[i-1]);
            BigInteger ny = numbers[i].multiply(result);
            BigInteger firstPart = ny.divide(two);
            // Tries both sqrt functions
            BigInteger secondPart = bigIntSqRootCeil(firstPart.pow(2).subtract(nm));
            BigInteger secondPartAlt = bigIntSqRootFloor(firstPart.pow(2).subtract(nm));
            result = firstPart.subtract(secondPart);
            resultAlt = firstPart.subtract(secondPartAlt);
        }

        System.out.println("The flag is stuyctf{" + result.toString() + "}");
        System.out.println("The flag is stuyctf{" + resultAlt.toString() + "}");
    }

    public static void main(String[] args) {
        revAlgorithm(5362426);
    }
}
