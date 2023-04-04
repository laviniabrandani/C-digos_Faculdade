public class Imovel {
    private String nome;
    private String endereco;
    private double valorDiaria;
    private boolean disponibilidade;
    private Proprietario proprietario;
    private Cliente cliente;

    public Imovel(String nome,
                  String endereco,
                  double valorDiaria,
                  boolean disponibilidade,
                  Proprietario proprietario
    ) {
        this.nome = nome;
        this.endereco = endereco;
        this.valorDiaria = valorDiaria;
        this.disponibilidade = disponibilidade;
        this.proprietario = proprietario;

    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public Proprietario getProprietario() {
        return proprietario;
    }
    public void setProprietario(Proprietario proprietario) {
        this.proprietario = proprietario;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public double getValorDiaria() {
        return valorDiaria;
    }

    public void setValorDiaria(double valorDiaria) {
        this.valorDiaria = valorDiaria;
    }

    public boolean getDisponibilidade() {
        return disponibilidade;
    }

    public void setDisponibilidade(boolean disponibilidade) {this.disponibilidade = disponibilidade;}

    public String consultarDadosDoImovel(){
        return "Nome: " + this.nome + "\n" +
                "Valor da Locação: " + this.valorDiaria + "\n" +
                "Endereço: " + this.endereco + "\n" +
                "Proprietario: " + this.proprietario.getNome() + "\n";
    }

    public double consultarValorLocacao(int quantidadeDias){
        return this.valorDiaria * quantidadeDias;
    }

    public String consultarSituacaoImovel(){
        if (this.disponibilidade){
            return "Disponivel"+ '\n';
        }else{
            return "Indisponivel para Aluguel"+ '\n';
        }
    }

    public boolean alugarImovel(Cliente cliente, int quantidadeDias){
        if(this.disponibilidade) {
            this.disponibilidade = false;
            this.cliente = cliente;
            return true;
        } else {
            return false;
        }
    }

    public void liberarImovel(){
        if(getDisponibilidade() == false){
            setDisponibilidade(true);
        }
    }
}
