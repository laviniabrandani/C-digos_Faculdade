public class Pessoa {

    //todos os atributos de uma classe deve ser privados, pq n pode permitir o acesso a nenhum atributo sem
    //ser através de um método

    //Atributos
    private String nome; //priva o conteúdo e so pode ser acessado apenas pela classe
    private int idade;
    private double peso;
    private double altura;
    private char sexo;

    // ====================================================

    //Método Construtor
    //pessoa é o método do tipo construtor, pois e a classe que vou usar para criar um objeto
    //toda classe tem um  método costrutor

    Pessoa(String nome, int idade, double peso, double altura, char sexo){
        this.nome = nome;
        this.idade = idade;
        this.peso = peso;
        this.altura = altura;
        this.sexo = sexo;
    }

    // ====================================================
    
    //Método Acessor (Get)

    public String getNome() {
        return this.nome;
    }

    public double getAltura(){
        return this.altura;

    }

    public int getIdade() {
        return idade;
    }

    public char getSexo() {
        return sexo;
    }

    public double getPeso() {
        return peso;
    }

    // ====================================================

    //Método  Mutante

    public void setNome(String nome){
        this.nome = nome;
    } //função sem retorno

    public void setAltura(double altura){
        this.altura = altura;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public void setSexo(char sexo) {
        this.sexo = sexo;
    }

    public double calcularImc(){
        return (this.peso / (this.altura * this.altura));
    }

    //alt+inset faz o seu método automático
}
