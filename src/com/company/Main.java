package com.company;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        BufferedImage img = null;
        File input = null;
        File output = null;
        File maskText = null;

        try {
            input = new File ("/Users/pedrocleis/IdeaProjects/PDI/img/lena256color.jpg");
            img = ImageIO.read(input);
            maskText = new File ("/Users/pedrocleis/IdeaProjects/PDI/img/mask.txt");
        } catch (IOException e){
            e.printStackTrace();
        }

        int width = img.getWidth();
        int height = img.getHeight();

        for (int i = 0; i < width; i++) {
            for (int j = 0; j < height; j++) {
                int pixel = img.getRGB(i,j);

                int r = 255 - (pixel>>16) & 0xff;
                int g = 255 - (pixel>>8) & 0xff;
                int b = 255 - pixel & 0xff;

                pixel = (r<<16) | (g<<8) | b;
                img.setRGB(i, j, pixel);
            }
        }

        try {
            output = new File ("/Users/pedrocleis/IdeaProjects/PDI/img/lena256colorR.jpg");
            ImageIO.write(img, "jpg", output);
        } catch (IOException e) {
            e.printStackTrace();
        }


        System.out.println("asd");
    }
}
