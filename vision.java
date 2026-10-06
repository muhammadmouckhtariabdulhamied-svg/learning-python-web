import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        // Load an image
        try {
            BufferedImage image = ImageIO.read(new File("speedometer.jpg"));

            // Convert the image to grayscale
            BufferedImage grayscaleImage = new BufferedImage(image.getWidth(), image.getHeight(), BufferedImage.TYPE_INT_RGB);
            for (int y = 0; y < image.getHeight(); y++) {
                for (int x = 0; x < image.getWidth(); x++) {
                    Color pixel = new Color(image.getRGB(x, y));
                    int grayValue = (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) / 3;
                    grayscaleImage.setRGB(x, y, grayValue);
                }
            }

            // Detect the speedometer
            int speedometerX = 0;  // Adjust this to match the actual location of the speedometer
            int speedometerY = 0;  // Adjust this to match the actual location of the speedometer
            int speedometerWidth = 100;  // Adjust this to match the actual width of the speedometer
            int speedometerHeight = 100;  // Adjust this to match the actual height of the speedometer
            int speedometerThreshold = 128;  // Adjust this to match the actual threshold for detecting the speedometer

            int count = 0;
            for (int y = speedometerY; y < speedometerY + speedometerHeight; y++) {
                for (int x = speedometerX; x < speedometerX + speedometerWidth; x++) {
                    Color pixel = new Color(grayscaleImage.getRGB(x, y));
                    int grayValue = (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) / 3;

                    if (grayValue > speedometerThreshold) {
                        count++;
                    }
                }
            }

            System.out.println("Count: " + count);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
