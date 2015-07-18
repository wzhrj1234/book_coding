class Human{
	public int getHeight(){
		return this.height;
	}
	public void growHeight(int h){
		this.height=this.height+h;
	}
	public void breath(){
		System.out.println("hu...hu...hu...");
	}
	private int height;
}

class Woman extends Human{
	public Human giveBirth(){
		System.out.println("Give birth ");
		return (new Human());
	}
	public void breath(){
		super.breath();
		System.out.println("su...");
	}
}

public class Testinheritance{
	public static void main(String[] args){
		Woman aWoman=new Woman();
		aWoman.growHeight(120);
		System.out.println(aWoman.getHeight());
		
	}
}