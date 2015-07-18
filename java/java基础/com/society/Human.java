package com.society;

public class Human{
	public Human(int h){
		this.height=h;
		System.out.println("I'm born");
	}
	public int getHeight(){
		return this.height;
	}
	public void growHeight(int h){
		this.height=this.height+h;
	}
	private int height;
}