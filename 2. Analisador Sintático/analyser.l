%{
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include "analyser.tab.h"
void yyerror(char *);
%}
%%

[a-z]    {
		yylval = *yytext - 'a';
		return VARIABLE;
		/* variables */
	 }


[0-9]+  {
		yylval = atoi(yytext);
		return INTEGER;
		/* integers */
	}


[-+(){}=/*\n]   { return *yytext;
		 /* operators */
		}
"[" 		{return *yytext;
		 /* operators */
		}
"]" 		{return *yytext;
		 /* operators */
		}
[ \t]    /* skip whitespace */;
.	yyerror("invalid character");        
	/* anything else is an error */


%%
int yywrap(void) {
	return 1;
}
