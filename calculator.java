import java.awt.*;
import java.awt.event.*;

public class calculator implements ActionListener {
    String s1, s2, s3, operator;
    Frame f;
    Button b0, b1, b2, b3, b4, b5, b6, b7, b8, b9;
    Button badd, bsub, bdiv, bmul, bclr, beq;
    Panel p;
    TextField t;
    GridLayout g;

    calculator() {
        f = new Frame("Calculator");
        f.setLayout(new FlowLayout());
        p = new Panel();

        b0 = new Button("0");
        b0.addActionListener(this);
        b1 = new Button("1");
        b1.addActionListener(this);
        b2 = new Button("2");
        b2.addActionListener(this);
        b3 = new Button("3");
        b3.addActionListener(this);
        b4 = new Button("4");
        b4.addActionListener(this);
        b5 = new Button("5");
        b5.addActionListener(this);
        b6 = new Button("6");
        b6.addActionListener(this);
        b7 = new Button("7");
        b7.addActionListener(this);
        b8 = new Button("8");
        b8.addActionListener(this);
        b9 = new Button("9");
        b9.addActionListener(this);

        badd = new Button("+");
        badd.addActionListener(this);
        bsub = new Button("-");
        bsub.addActionListener(this);
        bdiv = new Button("/");
        bdiv.addActionListener(this);
        bmul = new Button("X");
        bmul.addActionListener(this);
        bclr = new Button("C");
        bclr.addActionListener(this);
        beq = new Button("=");
        beq.addActionListener(this);

        t = new TextField(20);
        f.add(t);

        g = new GridLayout(4, 4);
        p.setLayout(g);

        p.add(b7);
        p.add(b8);
        p.add(b9);
        p.add(bdiv);
        p.add(b4);
        p.add(b5);
        p.add(b6);
        p.add(bmul);
        p.add(b1);
        p.add(b2);
        p.add(b3);
        p.add(bsub);
        p.add(b0);
        p.add(bclr);
        p.add(beq);
        p.add(badd);

        f.add(p);
        f.setSize(250, 200);

        f.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });

        f.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == b0) t.setText(t.getText() + "0");
        if (e.getSource() == b1) t.setText(t.getText() + "1");
        if (e.getSource() == b2) t.setText(t.getText() + "2");
        if (e.getSource() == b3) t.setText(t.getText() + "3");
        if (e.getSource() == b4) t.setText(t.getText() + "4");
        if (e.getSource() == b5) t.setText(t.getText() + "5");
        if (e.getSource() == b6) t.setText(t.getText() + "6");
        if (e.getSource() == b7) t.setText(t.getText() + "7");
        if (e.getSource() == b8) t.setText(t.getText() + "8");
        if (e.getSource() == b9) t.setText(t.getText() + "9");

        
        if (e.getSource() == badd) {
            s1 = t.getText();
            operator = "+";
            t.setText("");
        }
        if (e.getSource() == bsub) {
            s1 = t.getText();
            operator = "-";
            t.setText("");
        }
        if (e.getSource() == bmul) {
            s1 = t.getText();
            operator = "*";
            t.setText("");
        }
        if (e.getSource() == bdiv) {
            s1 = t.getText();
            operator = "/";
            t.setText("");
        }
        

        if (e.getSource() == bclr) {
            t.setText("");
            s1 = s2 = operator = null;
        }

        
        if (e.getSource() == beq) {
            s2 = t.getText();
            double result = 0;

            try {
                double num1 = Double.parseDouble(s1);
                double num2 = Double.parseDouble(s2);

                switch (operator) {
                    case "+" -> result = num1 + num2;
                    case "-" -> result = num1 - num2;
                    case "*" -> result = num1 * num2;
                    case "/" -> result = num1 / num2;
                }
                t.setText(String.valueOf(result));
            } catch (Exception ex) {
                t.setText("Error");
            }
        }
    }

    public static void main(String[] args) {
        new calculator();
    }
}
