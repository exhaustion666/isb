import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.Random;

/**
 * Generates a random binary sequence of length 128 bits
 * and saves it to the file "random_sequence.txt".
 *
 * This program uses the Random class to generate random sequence of 0 or 1.
 *
 * @throws Exception if an I/O error occurs while writing to the file
 */
public class Sequence {
    public static void main(String[] args) throws Exception {
        StringBuilder binarySequence = new StringBuilder(128);
        Random random = new Random();
        for (int i = 0; i < 128; i++)
            binarySequence.append(random.nextInt(2));
        BufferedWriter writer = new BufferedWriter(new FileWriter("random_sequence.txt"));
        writer.write(binarySequence.toString());
        writer.close();
    }
}
