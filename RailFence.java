import java.util.*;
class RailFence
{
	static String encryption(String text, int depth)
	{
		int r=depth;
		int c=text.length();
		boolean checkdown=false;
		char mat[][]= new char[r][c];
		String op="";

		int j=0;
		for(int i=0;i<c;i++)
		{
			if(j==0 || j==r-1)
			{
				checkdown=!checkdown;
			}
			mat[j][i]=text.charAt(i);
			if(checkdown)
				j++;
			else
				j--;
		}

		for(int i=0;i<r;i++)
		{
			for(int k=0;k<c;k++)
			{
				if(mat[i][k]!=0)
					op=op+mat[i][k];
			}
		}

		return op;
	}
	
	static String decryption(String text,int depth)
	{
		boolean checkdown=false;
		int r=depth;
		int c=text.length();
		char[][] mat=new char[r][c];

 		int j=0;
		for(int i=0;i<c;i++)
		{
			if(j==0 || j==r-1)
			{
				checkdown=!checkdown; 
			} 
			mat[j][i]='*';
			if(checkdown)
				j++;
			else 
				j--;
		}
 
		int index=0;
		for(int i=0;i<r;i++)
		{
			for(int k=0;k<c;k++)
			{
				if(mat[i][k]=='*' && index<text.length())
				{
					mat[i][k]=text.charAt(index++);  
				}
			}
		}
  
		checkdown=false;
		String op="";
		j=0;
		for(int i=0;i<c;i++)
		{
			if(j==0 || j==r-1)
				checkdown=!checkdown;
			op+=mat[j][i];
			if(checkdown)
				j++;
			else 
				j--;
		}
		return op;
	}

	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter the plain text: ");
		String plaintext=sc.nextLine();
		System.out.print("Enter the key: ");
		int key=sc.nextInt();
		//String p="THISISASECRETMESSAGE";
		String encrypt=encryption(plaintext,key);
		System.out.println("Text after encryption: "+encrypt);
		System.out.println("Text after decryption: "+decryption(encrypt,key));
	}
}