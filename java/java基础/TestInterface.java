public class TestInterface{
	public static void main(String[] args){
		MusicCup cup1 = new MusicCup();
		cup1.showWater();
		cup1.addWater(100);
		cup1.showWater();
		cup1.drinkWater(50);
		cup1.showWater();
	}
}

interface Cup{
	void addWater(int w);
	void drinkWater(int w);
}

class MusicCup implements Cup{
	public void addWater(int w){
		this.water=this.water+w;
	}
	public void drinkWater(int w){
		this.water=this.water-w;
	}
	public void showWater(){
		System.out.println(this.water);
	}

	private int water=0;
}