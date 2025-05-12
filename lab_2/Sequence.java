import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.Random;

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
