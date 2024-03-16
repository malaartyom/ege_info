package ru.nsu.mmf.syspro.forth;

import ru.nsu.mmf.syspro.forth.exceptions.InterpreterException;
import ru.nsu.mmf.syspro.forth.exceptions.InterpreterExitException;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Interpreter interpreter = new Interpreter();
        while (true) {
            String line = scanner.nextLine();
            try {
                InterpreterResult result = interpreter.interpret(line);
                System.out.println(result.out());
                if (result.exit()) {
                    return;
                }
            } catch (InterpreterException e) {
                if (e instanceof InterpreterExitException) {
                    break;
                }
                System.err.println(e.getMessage());
            }
        }
    }
}

