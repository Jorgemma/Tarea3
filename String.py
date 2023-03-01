import java.lang.ProcessBuilder.Redirect.Type;
import java.util.Comparator;
import java.util.Scanner;

import org.w3c.dom.TypeInfo;
public class gato {
    public static void main(String[]args) {
        Scanner in= new Scanner(System.in);
        int A=0,control=0,Si=0;
        System.out.println("Impresor del juego del gato");
        while(A==0){
            System.out.println("Ingrese la cadena de 9 caracteres solo compuesta de X,O,_: ");
            String Entrada=in.nextLine();
            String EntradaMay=Entrada.toUpperCase();
            String[]divicion=EntradaMay.split("");
            
            for (int j = 0; j < divicion.length; j++) {
                if (divicion[j].equals("X") || divicion[j].equals("O") || divicion[j].equals("_")) {
                    Si=Si+1;
                }
            }
            if(EntradaMay.length()==9){
                if (Si==9) {
                    control=0;
                    for (int index = 0; index < 5; index++) {
                        if (index==0 || index==4) {
                            System.out.println("l  l  l  l  l");
                        }
                        else{
                            System.out.println("l  "+divicion[0+control]+"  "+divicion[1+control]+"  "+divicion[2+control]+"  l");
                            control+=3;
                        }
                        A=1;
                    }
                }else{
                    System.out.println("Solo se permiten X,O,_");
                }
                
            }else{
                System.out.println("Se necesitan a fuerzas 9 caracteres, vuelve a intentar");
            }
        }
    }
}
