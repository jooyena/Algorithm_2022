#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

int N,top[50],sum=0
int dp[50][50001];

int main(void){
	ios::sync_with_stdio(fasle);
	cin.tie(0); cout.tie(0);
	
	cin>>N;
	
	for(int i=0;i<N;i++){
		cin>> top[i];
		sum+=top[i];
	}
	
	memset(dp, -1, sizeof(dp));
	
	dp[0][0]=0;
	dp[0][top[0]]=top[0]; //Ã³À½ ½×±â
	 
	for(int i=0; i<N; i++){
		for(int j=0; j< sum; j++){
			if(dp[i][j]==-1) continue;
		
			//½×Áö ¸»±â
			dp[i][j] = max(dp[i][j],dp[i-1][j])
		
			// Å« ÂÊ¿¡ ½×±â
			dp[i+1][j+top[i+1]] = max(dp[i][j+top[i]],dp[i-1][j]+top[i]]);
			
			// ÀÛÀº ÂÊ¿¡ ½×±â
			if(j < top[i]) dp[i][top[i]-j] = max(dp[i][top[i]-j], dp[i-1][j]-j+top[i]);
			if(j>=top[i]) dp[i][j-top[i]] = max(dp[i][j-top[i]],dp[i-1][j]); 
				
		}
	}
	dp[N-1][0] ? cout << dp[N-1][0]: cout<< -1
	return 0;
}
