public class TestClass{
	public static void main(String[] args){
		Human apeople = new Human(170,"Henry");
		System.out.println(apeople.getHeight());
		apeople.growHeight(10);
		System.out.println(apeople.getHeight());
		apeople.repeatBreath(5);
	}
}

class Human{
	//constructor
	public Human(int h){
		this.height=h;
		System.out.println("I'm born!");
	}
	//mothod overloading
	public Human(int h , String s){
		this.height=h;
		System.out.println(s+" is born!");
	}
	private void breath(){
		System.out.println("hu..hu..");
	}
	public int getHeight(){
		return this.height; 	// this 不是必须的，可以写成 return height;
	}
	public void growHeight(int h){
		this.height=this.height+h;
	}
	public void repeatBreath(int rep){
		for(int i=0;i<=rep;i++){
			this.breath();		//调用类本身的函数
		}
	}
	private int height;
}