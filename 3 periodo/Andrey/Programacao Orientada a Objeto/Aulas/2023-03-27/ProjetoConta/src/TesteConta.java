public class TesteConta {
    public static void main(String[] args) {
        Cliente cliente1 = new Cliente(
                "Felipe",
                "999.999.999-99",
                "Rua Y, numero 2");
        Conta conta1 = new Conta(
                123,
                "Corrente",
                4455,
                cliente1);

        Cliente cliente2 = new Cliente(
                "Joana",
                "888.888.888-88",
                "Rua Z, numero 20");
        Conta conta2 = new Conta(
                123,
                "Poupança",
                2277,
                cliente2);
        Conta conta3 = new Conta(
                123,
                "Corrente",
                3355,
                cliente2);

        if (conta1 == conta2){
            System.out.println("As contas são iguais");
        }else{
            System.out.println("As contas são diferentes");
        }

        //Conta conta3 = conta2;

        System.out.println(conta1.getTitular().getNome());
        System.out.println(conta2.getTitular().getNome());
        System.out.println(conta3.getTitular().getNome());

        cliente2.setNome("Joana Souza");
        System.out.println(conta2.getTitular().getNome());
        System.out.println(conta3.getTitular().getNome());

        conta1.depositarValor(500);
        conta1.depositarValor(200);

        conta1.sacarValor(100);
        boolean saqueRealizado = conta1.sacarValor(1000);

        if(saqueRealizado == true){
            System.out.println("Saque Realizado com Sucesso");
        }else {
            System.out.println("Saque não realizado");
        }

        System.out.println(conta1.getSaldo());
    }
}
