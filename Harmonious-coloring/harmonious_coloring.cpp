#include<fstream>
#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<cstring>
#include <stdlib.h>
#define N 50
#define MAX_LINE 1024
using namespace std;


int n,max_current=N+0;
vector<int> adj[N];
int colors[N]; //current partial coloring
int x[N]; //current partial coloring, generated using backtracking
int min_colors[N]={N};//best coloring obtained 


ifstream f;
vector<int> neighbours_color[N]; //neighbour_colors[j] = list of the colors used for neighbors of color j 

void back(int k);
int diameter();
 
int diameter(){
	int a[N+1][N+1];
	int i,j,k;
	for(i=0;i<=n;i++)
		for(j=0;j<=n;j++)
			a[i][j]=n+1;
	
	for(i=0;i<n;i++){
		a[i][i]=0;
		for(j=0;j<adj[i].size();j++)
			a[i][adj[i][j]]=1;
		}
	


	int diam=0;
	for(k=0;k<n;k++)
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(a[i][j]>a[i][k]+a[k][j])
					a[i][j]=a[i][k]+a[k][j];
	
	
	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			if(diam<a[i][j] && a[i][j]<n+1)
				diam=a[i][j];
	
	return diam;
}
 




int color_graph(){
    colors[0]=1;
    neighbours_color[1].push_back(0);
    back(1);
}
    

void print_to_file(ofstream &h){
	

	h<<"h = "<<*max_element(min_colors,min_colors+n)<<endl;
	for(int j=0;j<n;j++)
		h<<min_colors[j]<<"  ";
	h<<endl;
	h<<"diameter = "<<diameter()<<endl; 
	h<<endl;

}



int check(int k){
	int c,i,u,j;
    if (*max_element(colors,colors+n)==0)
        return 1;

    set<int> neighbour_current_color;//neighbor colors of current color colors[k]
    for(int j=0;j<neighbours_color[colors[k]].size();j++){
	    int v=neighbours_color[colors[k]][j];
		c=colors[v];
         
		
        for(i=0;i<adj[v].size();i++){
			u=adj[v][i];
			if (colors[u]!=0){
				
				if (neighbour_current_color.find(colors[u])!= neighbour_current_color.end()  )
                   	return 0;
                
                neighbour_current_color.insert(colors[u]);
            }
        }
        
	}
    return 1;
}



void back(int k){
	int i,t;
	if (k==n){
	    if (*max_element(colors,colors+n)<*max_element(min_colors,min_colors+n)){
        	for(t=0;t<n;t++)
        		min_colors[t]=colors[t];
        	max_current=*max_element(min_colors,min_colors+n);
		}
    }
    else{
	  
		    int limit=min(*max_element(colors,colors+n)+1,max_current-1);
			for(i=1;i<=limit;i++){
		    	colors[k]=i;
		        neighbours_color[i].push_back(k);
	            if (check(k))
	                back(k+1);
	            neighbours_color[i].pop_back();
	            colors[k]=0;
            }
        
    }

}
void read_graph(){
	int x,y;
    f.open("harmonious.in");
    
   	f>>n;
 
    while(f>>x>>y){
        adj[x-1].push_back(y-1);
        adj[y-1].push_back(x-1);
    }
    f.close();
}

int a[N+1][N+1];



void read_and_color_graphs(){
	int x,y,no_graphs,i,j,v,u;
	char graph_name[MAX_LINE],line[MAX_LINE],*p;
    f.open("harmonious_adj.in");
   	f>>n;
   	f>>no_graphs;
   	f.get();
    ofstream h("harmonious.out");
   	
   	for(i=0;i<no_graphs;i++){
   		for(j=0;j<=n;j++){
		    colors[j]=0;
			min_colors[j]=N+1;
   			adj[j].clear();
   			neighbours_color[j].clear();
   		}
   		f.getline(graph_name,MAX_LINE);
   		h<<graph_name<<endl;
   		for(j=0;j<n;j++){
   			f.getline(line,MAX_LINE);
   			p=strtok(line," ");
   			v=atoi(p);
   			p=strtok(NULL," ");
   			while(p){
   				u=atoi(p);
   				adj[v-1].push_back(u-1);
   				p=strtok(NULL," ");
			}
   			
		}
		max_current=N+1; 
		color_graph();
		print_to_file(h);
	}
   	
    
    f.close();
}
    
int main(){
	ofstream h("harmonious.out");
	cout<<"1. Harmonious chromatic number of a graph given by list of edges"<<endl;
	cout<<"2. Harmonious chromatic number of a set of graphs given by adjacent list"<<endl;
	cout<<"Your choice (1 or 2):";
	int option;
	cin>>option;
	if(option==1){
		read_graph();
		color_graph();
		print_to_file(h);
		h.close();	
		return 0;
	}
	if(option==2){
		read_and_color_graphs();
		return 0;
	}
	cout<<"Invalid option";
	return 1;
	
}



