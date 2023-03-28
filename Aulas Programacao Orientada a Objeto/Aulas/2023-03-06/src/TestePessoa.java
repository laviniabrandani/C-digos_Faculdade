import javax.swing.plaf.synth.SynthOptionPaneUI;

public class TestePessoa {
    public static void main(String[] args) {

        //A partir do new eu instancio um objeto, ela é um objeto
        // do tipo pessoa (um ojeto que tem as caracteristicas do tipo pessoa)
        // criar um objeto, uso o metodo construtor para obrigar o valor daquele objeto

        Pessoa pessoaJose = new Pessoa("Jose", 47, 78.5, 1.70, 'M');
        Pessoa pessoaMaria = new Pessoa("Maria", 30, 65, 1.60, 'F');
        Pessoa pessoaJoao = new Pessoa("Jao", 25, 70, 1.78, 'M');

        //pessoaJose.nome = "José";
        //pessoaJose.idade = 47;
        //pessoaJose.peso = 78.5;
        //pessoaJose.altura = 1.70;
        //pessoaJose.sexo = 'M';


        //Pessoa pessoaMaria = new Pessoa();
        //pessoaMaria.nome = "Maria";
        //pessoaMaria.idade = 30;
        //pessoaMaria.peso = 65;
        //pessoaMaria.altura = 1.60;
        //pessoaMaria.sexo = 'F';


        //Pessoa pessoaJoao = new Pessoa();
        //pessoaJoao.nome = "João";
        //pessoaJoao.idade = 25;
        //pessoaJoao.peso = 70;
        //pessoaJoao.altura = 1.78;
        //pessoaJoao.sexo = 'M';

        //System.out.println(pessoaJose.getNome());
        //System.out.println(pessoaMaria.idade);
        //System.out.println(pessoaJoao.peso);
        //pessoaJose.setNome("Mimi");
        //System.out.println(pessoaJose.getNome());

        System.out.println("O IMC da Maria é: " + pessoaMaria.calcularImc());

        System.out.println("A altura da Maria é : " + pessoaMaria.getAltura());
        System.out.println("A altura da Jose é : " + pessoaJose.getAltura());

    }
}
