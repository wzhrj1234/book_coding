import java.io.*;

public class TestIO{
	public static void main(String[] args){
		try{
			BufferedReader br=new BufferedReader(new FileReader("file.txt"));
			String line=br.readLine();
			while(line!=null){
				System.out.println(line);
				line=br.readLine();
			}
			br.close();
		}
		catch(IOException e){
			System.out.println("IO Problem");
		}
		try{
			String content="Thank you for your fish.";
			File file=new File("new.txt");
			if(!file.exists()){
				file.createNewFile();
			}
			FileWriter fw=new FileWriter(file.getAbsoluteFile());
			BufferedWriter bw =new BufferedWriter(fw);
			bw.write(content);
			bw.close();
		}
		catch(IOException e){
			System.out.println("IO Problem");
		}
	}
}