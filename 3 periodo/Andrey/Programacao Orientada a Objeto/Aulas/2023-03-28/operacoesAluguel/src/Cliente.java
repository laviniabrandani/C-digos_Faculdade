public class Cliente {
    private String nome;
    private String endereco;
    private String cpf;
    private String email;
    private String telefone;


    public Cliente(String nome,
                   String endereco,
                   String cpf,
                   String email,
                   String telefone) {
        this.nome = nome;
        this.endereco = endereco;
        this.cpf = cpf;
        this.email = email;
        this.telefone = telefone;
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

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public String consultarDadosDoCliente(){
        return "Nome do Cliente: " + this.nome + "\n" +
                "Endereço: " + this.endereco + "\n" +
                "Telefone: " + this.telefone;
    }
}
