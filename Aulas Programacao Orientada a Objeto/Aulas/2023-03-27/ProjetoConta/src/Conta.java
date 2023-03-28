public class Conta {
    private int agencia;
    private String tipo;
    private int numero;
    private double saldo;
    private Cliente titular;

    public Conta(int agencia, String tipo, int numero, Cliente titular) {
        this.agencia = agencia;
        this.tipo = tipo;
        this.numero = numero;
        this.saldo = 0.0;
        this.titular = titular;
    }

    public int getAgencia() {
        return agencia;
    }

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

    public Cliente getTitular() {
        return titular;
    }

    public void setTitular(Cliente titular) {
        this.titular = titular;
    }

    public void depositarValor(double valorDepositado){
        this.saldo += valorDepositado;
    }

    public boolean sacarValor(double valorSaque){
        if(this.saldo >= valorSaque){
            this.saldo = this.saldo - valorSaque;
            //this.saldo -= valorSaque;
            return true;
        }else {
            return false;
        }
    }
}
