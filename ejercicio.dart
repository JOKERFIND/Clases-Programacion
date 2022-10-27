//--------------------------------------------------------------------------------------------------------------------
//void main () {
//  var usuario1 = user(); //instancia de la clase user
//  usuario1._nombre="Alex";
//  usuario1._edad=50;
//  usuario1.reporte();
//}
//
////encapsulamiento
////- ocultar los atributos de la clase
////- hacerlos locales dentro de la clase
////- el sistema 
//
//class user {
// //propiedades
// string? _nombre;
// int? _edad;
// //Metodos
// void reporte(){
//  print(_nombre);
//  print(_edad);
// }
//}
//
//void main(List<String>args){
// user usuario1=user();
// usuario1.nombre="Alex";
// usuario1.edad=15;
// //print(usuario1.nombre);
// usuario1.reporte();
//}
//
//class user{
// String? _nombre;
// int? _edad;
//
// void set nombre(String nombre) {
//  _nombre = nombre ;
// }
//
//void set edad(int edad) -> _edad=edad;
//
//String get nombre ->_nombre!;
//
//string get edad->_edad!;
//
// void reporte(){
//  print(_nombre);
//  print(_edad);
// }
//}
//--------------------------------------------------------------------------------------------------------------
////Una calculadora que sume, reste, multiplique y divida
//
//void main(List<String> args){
//// print(suma(1,2));
//// var res = suma(2,3);
//// print(res);
//calculadora miSC=calculadora();
//
//miSC.a=5;
//miSC.b=10;
//
//int res= miSC.suma(miSC.a, miSC.b)
//print("${miSC.a} + ${miSC.b= res}");
//}
//calculadora miSC=calculadora();
//int n1, n2;
//n1=5;
//N2=10;
//
//int res=miSC.suma(n1, n2);
//print("$n1 + $n2 = $res");
//print("$n1, $n2 = ${miSC.suma(n1 + 1, n2 + 3)})");
//
//void calculadora {
// int a=0;
// int b=0;
// int suma(a + b)
// int resta(int a, int b) --> a - b;
// int multi(int a, int b)  --> a*b; 
//double divi(lint a, lint b) --> a/b;
//}
//--------------------------------------------------------------------------------------------------------------
//void main(){
//  estudiante1.carrera="Ingenieria en Computacion Inteligente";
//  estudiante1.noCuenta= "8734434";
//  estudiante1.semestre= "3";
//  estudiante1.reporte();
//}
//
//class Estudiante {
//string? noCuenta;
//string? carrera;
//int? semestre;
//
// void reporte(){
//  print("Carrera           :$carrera");
//  print("No de Cuenta:$noCuenta");
//  print("Semestre       :$semestre");
//  
// }
//}
//--------------------------------------------------------------------------------------------------------------
//void main() {
//  var carro = new Vehiculo(4, 'Azul', 'Jeep', 'Rubicon');
//  print(carro.arrancar());
//  print(carro.avanzar());
//  print(carro.frenar());
//  print(carro.color);
//}
//
//class Vehiculo {
//  int _nmLlantas = 4;
//  String _color = 'Blanco';
//  String _marca = 'Ford';
//  String _modelo = 'Fiesta';
//  String arrancar() => 'Arrancando';
//  String avanzar() => 'Avanzando';
//  String frenar() => 'Frenando';
//
//  void set color(String color) => _color = color;
//  void set marca(String marca) => _marca = marca;
//  void set modelo(String modelo) => _modelo = modelo;
//  void set nmllantas(int llantas) => _nmLlantas = llantas;
//
//  String get color => _color;
//  String get marca => _marca;
//  String get modelo => _modelo;
//  int get nmllantas => _nmLlantas;
//  
//  //Vehiculo(int llantas, String color, String marca, String modelo) {
//  //  this._color = color;
//  //  this._marca = marca;
//  //  this._modelo = modelo;
//  //  this._noLlantas = llantas;
//  //}
//  
//  Vehiculo(this._noLlantas, this._color, this._marca, this._modelo);
//}

//---------------------------------------------------------------------------------------------------------------
//void main() {
// gato pedro = gato();
// print("--------------------------------");
// pedro.caminando();
// pedro.raza();
// pedro.nombre();
// pedro.especie();
// pedro.patas();
// print("--------------------------------");
//}
//
//
//class animal{
// String _especie='felino';
// int _nmpatas=4;
// String _color='blanco';
// void caminando()=>print('Accion: "'"animal caminando"'"');
//}
//
//class gato extends animal{
//    String _raza='cymric';
//    String _clr_ojos='amarillo';
//    void caminando()=>super.caminando();
//    void raza()=>print('Raza: "'"$_raza"'"');
//    void nombre()=>print('Nombre: "'"pedro"'"');
//    void especie()=>print('Especie: "'"$_especie"'"');
//    void patas()=>print('Patas: $_nmpatas');
//}