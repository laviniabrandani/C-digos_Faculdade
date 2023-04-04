public class Conta {

    private int agencia;
    private String tipo;
    private int numero;
    private double saldo;
    private String titular;

    public Conta(int agencia, String tipo, int numero, String titular) {
        this.agencia = agencia;
        this.tipo = tipo;
        this.numero = numero;
        this.saldo = 0.0;
        this.titular = titular;
    }
    public void depositarValor(double valorDepositado){
        this.saldo = this.saldo + valorDepositado;
    }
    public boolean sacarValor(double valorSaque){
        if (this.saldo >= valorSaque) {
            this.saldo = this.saldo - valorSaque;
            return true;
        }else{
            return false;
        }

    }

    /*get pega informacao e set guarda informacao */
    public int getAgencia() {
        return agencia;
    }
    /*metodos do tipo Void nao retornar nada para quem chamou a funcao */
    public void setAgencia(int agencia) {
        this.agencia = agencia;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public String getTitular() {
        return titular;
    }

    public void setTitular(String titular) {
        this.titular = titular;
    }
}
