/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package test;

import java.math.BigDecimal;
import java.math.BigInteger;

/**
 *
 * @author ABCD
 */
public class Test extends Test2 {

    /**
     * @param args the command line arguments
     */
    public static BigInteger numbers[] = {BigInteger.valueOf(3570793128L),
        BigInteger.valueOf(1458104314),
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

    public static BigDecimal reverseAlgorithm(BigDecimal input, BigInteger[] numbers, int length_numbers) {
        BigDecimal result = input;
        int i;
        for (i = 22; i >= 1; --i) {
            result = formula(result, numbers[i], numbers[i - 1]);
            System.out.println(result);
            System.out.println(i);
        }
        System.out.println("\n");
        return result;
    }

    public static BigDecimal formula(BigDecimal x, BigInteger c, BigInteger d) {
        
        // Variables
        BigDecimal newC = new BigDecimal(c);
        BigDecimal newD = new BigDecimal(d);
        
        // Integers
        BigDecimal new2 = new BigDecimal(2);
        BigDecimal new4 = new BigDecimal(4);
        BigDecimal newHalf = new BigDecimal(.5);
        
        // Calculations
        BigDecimal product = newC.multiply(x);
        BigDecimal squareStep1 = product.multiply(product).subtract(newC.multiply(newD).multiply(new4));
        BigDecimal squareStep2 = sqrt(squareStep1);
        System.out.println(squareStep2);

        // ROOTS
        BigDecimal positiveR = newHalf.multiply(product.add(squareStep2));
        BigDecimal negativeR = newHalf.multiply(product.subtract(squareStep2));
        System.out.println(positiveR);

        if (positiveR.compareTo(negativeR) > 0) {
            return positiveR;
        } else {
            return negativeR;
        }
    }
    public static BigDecimal sqrt(BigDecimal value) {
        BigDecimal x = new BigDecimal(Math.sqrt(value.doubleValue()));
        return x.add(new BigDecimal(value.subtract(x.multiply(x)).doubleValue() / (x.doubleValue() * 2.0)));
    }

    public static void main(String[] args) {
        BigDecimal computer = new BigDecimal(5362426);
        System.out.println(reverseAlgorithm(computer, numbers, 23));
	//printf("\n%lu\n", algorithm((long) reverseAlgorithm(computer, numbers, NUMBER_OF_RANDOMS), numbers, 23));
    }

}
