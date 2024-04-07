import java.util.*;
class Columnar
{
	static String encryption(String text,String key,int row,int column)
	{
		char mat[][]=new char[row][column];
		int index=0;
		for(int i=0;i<row;i++)
		{
			for(int j=0;j<column;j++)
			{
				if(index<text.length())
				{
					mat[i][j]=text.charAt(index++);
				}
				else
				{
					mat[i][j]=' ';
				}
			}
		}
		
		char keyarr[]=key.toCharArray();
		char sortedkey[]=key.toCharArray();
		for(int i=0;i<column-1;i++)
		{
			for(int j=i+1;j<column;j++)
			{
				if(sortedkey[i]>sortedkey[j])
				{
					char temp=sortedkey[i];
					sortedkey[i]=sortedkey[j];
					sortedkey[j]=temp;
				}
			}
		}

		char encrypt[][]=new char[row][column];
		for(int i=0;i<column;i++)
		{
			for(int j=0;j<column;j++)
			{
				if(keyarr[i]==sortedkey[j])
				{
					for(int k=0;k<row;k++)
					{
						encrypt[k][j]=mat[k][i];
					}
					sortedkey[j]='?';
					break;
				}
			}
		}
		
		String op="";
		for(int i=0;i<column;i++)
		{
			for(int j=0;j<row;j++)
			{
				op=op+encrypt[j][i];
			}
		}
		return op;
	}

	static String decryption(String text,String key,int row,int column)
	{
		char mat[][]=new char[row][column];
		int index=0;
		for(int i=0;i<column;i++)
		{
			for(int j=0;j<row;j++)
			{
				if(index<text.length())
				{
					mat[j][i]=text.charAt(index++);
				}
			}
		}
		
		char keyarr[]=key.toCharArray();
		char sortedkey[]=key.toCharArray();
		for(int i=0;i<column-1;i++)
		{
			for(int j=i+1;j<column;j++)
			{
				if(sortedkey[i]>sortedkey[j])
				{
					char temp=sortedkey[i];
					sortedkey[i]=sortedkey[j];
					sortedkey[j]=temp;
				}
			}
		}

		char decrypt[][]=new char[row][column];
		for(int i=0;i<column;i++)
		{
			for(int j=0;j<column;j++)
			{
				if(keyarr[j]==sortedkey[i])
				{
					for(int k=0;k<row;k++)
					{
						decrypt[k][j]=mat[k][i];
					}
					keyarr[j]='?';
					break;
				}
			}
		}
		
		String op="";
		for(int i=0;i<row;i++)
		{
			for(int j=0;j<column;j++)
			{
				op=op+decrypt[i][j];
			}
		}
		return op;
	}
	
	public static void main(String args[])
	{
		int row,column,choice;
		Columnar obj=new Columnar();
		System.out.print("Enter plain text: ");
		Scanner sc=new Scanner(System.in);
		String str=sc.nextLine();
		System.out.print("Enter the key: ");
		String key=sc.nextLine();
		row=str.length()/key.length();
		if(str.length()%key.length()!=0)
		{
			row++;
		}
		column=key.length();
		String encryptext=encryption(str,key,row,column);
		System.out.println("Text after encryption: "+encryptext);
		System.out.println("Text after decryption: "+decryption(encryptext,key,row,column));
	}
}