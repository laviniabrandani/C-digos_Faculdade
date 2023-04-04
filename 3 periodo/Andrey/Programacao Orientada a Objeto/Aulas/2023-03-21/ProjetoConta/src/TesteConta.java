public class TesteConta {
    public static void main(String[] args) {
        Conta conta1 = new Conta(
                123,
                "Corrente",
                4455,
                "Felipe");

        Conta conta2 = new Conta(
                123,
                "Poupança",
                2277,
                "Joana"
        );

//        conta1.setTitular("Titular 1");
//        conta1.setTipo("Corrente");
//
//        conta2.setTitular("Titular 1");
//        conta2.setTipo("Corrente");


//        if(conta1 == conta2){
//            System.out.println("As contas são iguais");
//        }else{
//            System.out.println("As contas são diferentes");
//        }
        //Conta conta3 = conta2;
        System.out.println(conta1.getTitular());
        System.out.println(conta2.getTitular());


//        conta1.depositarValor(500);
//        conta1.depositarValor(200);
        conta1.sacarValor(100);
        boolean saqueRealizado = conta1.sacarValor(1000);
        if(saqueRealizado == true){
            System.out.println("Saque Realizado com Sucesso!");
        }else{
            System.out.println("Saque Não Realizado");
        }

        System.out.println(conta1.getSaldo());
    }
}
