public class TesteAluguel {
    public static void main(String[] args) {
        //1
        Cliente cliente1 = new Cliente(
                "Luiz Otávio dos Santos",
                "Rua X, número 8",
                "145.789.656-45",
                "luizotavio@email.com",
                "(35) 99858-4584");
        //2
        System.out.println(cliente1.consultarDadosDoCliente() + "\n");

        Cliente cliente2 = new Cliente(
                "Lavinia Rodrigues Brandani",
                "Rua Y, número 10",
                "149.812.586-48",
                "lavinia@gmail.com",
                "(35) 99785-6932");

        //3
        Proprietario proprietario1 = new Proprietario(
                "Felipe Souza",
                "Rua Nova, número 56",
                "125.478.899-99",
                "felipe@email.com",
                "(35) 98784-5698");
        //4
        System.out.println(proprietario1.consultarDadosDoProprietario() + "\n");

        //5
        Imovel imovel1 = new Imovel(
                "Apartamento para 4 pessoas",
                "Rua da Saudade, número 245",
                145.75,
                true,
                proprietario1);

        //6
        System.out.println(imovel1.consultarDadosDoImovel() + "\n");

        //7
        double valorDaLocacao = imovel1.consultarValorLocacao(7);
        System.out.println("O valor do aluguel para 7 dias é: " + valorDaLocacao + "\n");

        //8
        System.out.println("O imóvel encontra-se: " + imovel1.consultarSituacaoImovel() + "\n");

        //9
        boolean alugar1 = imovel1.alugarImovel(cliente1, 7);
        if(alugar1) {
            System.out.println("Voce alugou o imóvel" + '\n');
        } else {
            System.out.println("O imóvel ja esta alugado"+ '\n');
        }

        //10
        System.out.println(imovel1.consultarSituacaoImovel());

        //11
        boolean alugar2 = imovel1.alugarImovel(cliente2, 5);
        if(alugar2) {
            System.out.println("Voce alugou o imóvel"+ '\n');
        } else {
            System.out.println("O imóvel ja esta alugado"+ '\n');
        }

        //12
        imovel1.liberarImovel();

        //13
        System.out.println(imovel1.consultarSituacaoImovel());
    }
}
