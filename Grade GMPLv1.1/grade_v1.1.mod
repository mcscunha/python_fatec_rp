/*------------------------------------------------------------------------------
Documento: Modelo para geração de grade horária
Descrição: Modelo com análise de infactibilidade por falta de disponibilidade de horário
Autor: Júnior César Bonafim (jrbonafim@gmail.com)
--------------------------------------------------------------------------------
Versão: 1.1
Última modificação: 01/05/2018
------------------------------------------------------------------------------*/



/*------------------------------------------------------------------------------
               Conjuntos     e     dados    iniciais
------------------------------------------------------------------------------*/

set disciplinas dimen 6;
set cod;
set disp_cod dimen 4;
param T;
set hor:=1..T;
param S;
set semestres:=1..S;
set professores;
set cursos;
set diasN;
set periodo;
param elemN{i in 1..card(diasN)}, symbolic, in diasN;
param seg{cod};
param ter{cod};
param qua{cod};
param qui{cod};
param sex{cod};
param sab{cod};
param cont:=0;



/*
table tab_disciplinas IN "CSV" "disciplinas.csv" :
   disciplinas <- [Disciplina,Professor,Curso,Periodo,Semstre,Ch];
*/

table tab_dispo_teste IN "CSV" "dispo_teste.csv" :
   disp_cod <- [professor, periodo, hor, cod];

table tab_dispo_teste IN "CSV" "dispo_teste.csv" :
   cod <- [cod], seg~seg, ter~ter,qua~qua, qui~qui, sex~sex, sab~sab;

#'DSN=PostgreSQL30'
#Server servidor rodando a base de dados (localhost por padrão);
#Database nome da base de dados;
#UID nome de usuário;
#PWD senha de usuário;
#Port porta usada pelo servidor (3306 por padrão).
table t_disciplinas IN 'ODBC' 
   "SERVER=tccsge2018.colyonzwqpbv.us-east-2.rds.amazonaws.com;"
   "DATABASE=dbtccsge2018;UID=usrpsg;PWD=Heliw73%;PORT=5432"
   'SELECT * FROM t_disciplinas;': 
   disciplinas <- [disciplina,professor,curso,periodo,semestre,ch];

# printf disciplinas;

# exit;

table tab_professores IN "CSV" "professores.csv" :
  professores <- [profs];  
  
table tab_diasN IN "CSV" "diasN.csv" :
  diasN <- [dias];  
  

table tab_cursos IN "CSV" "cursos.csv" :
  cursos <- [cursos]; 

table tab_periodo IN "CSV" "periodo.csv" :
  periodo <- [periodo]; 
  
  
param Disp{i in cod,j in diasN}
:= if j = "seg" then seg[i] else
  if j = "ter" then ter[i] else
    if j = "qua" then qua[i] else
      if j = "qui" then qui[i] else
        if j = "sex" then sex[i] else
          if j = "sab" then sab[i] else 23;


param ideal :=sum{(a,b,c,d,e,f) in disciplinas}f;

param Disp_ideal{p in professores, l in periodo};


param txt, symbolic := "result.txt";

 param txt2, symbolic := "result2.txt";
 
  param txt3, symbolic := "result3.txt";

/*param teste{i in hor, j in diasN}, symbolic;*/

  var x{(a,b,c,d,e,f) in disciplinas,j in diasN,hor} binary;
  var print{c in cursos, p in periodo} binary;
  var sem{c in cursos, p in periodo} >=0 integer;
  # disc, prof, curso, periodo, sem ,ch
  

  
/*------------------------------------------------------------------------------
                          Função        Objetivo
------------------------------------------------------------------------------*/
  
 /* minimize total: sum{(a,b,c,d,e,f) in disciplinas,k in hor:d="Noite"} x[a,b,c,d,e,f,"sab",k] + sum{(a,b,c,d,e,f) in disciplinas, j in diasN:d!="Noite"} x[a,b,c,d,e,f,j,3];*/
  
maximize total2: sum{(a,b,c,d,e,f) in disciplinas,
(a1,b1,c1,d1) in disp_cod, k in hor, j in diasN:a1=b && b1=d && c1=k} 2*x[a,b,c,d,e,f,j,k]*Disp[d1,j] - sum{(a,b,c,d,e,f) in disciplinas,k in hor:d="Noite"} x[a,b,c,d,e,f,"sab",k] - sum{(a,b,c,d,e,f) in disciplinas, j in diasN:d!="Noite"} x[a,b,c,d,e,f,j,3]; 
  


/*------------------------------------------------------------------------------
                             Restrições         
------------------------------------------------------------------------------*/

/* Respeita disponibilidade do professor */

/* R0{(a,b,c,d,e,f) in disciplinas,
(a1,b1,c1,d1) in disp_cod, k in hor, j in diasN:a1=b && b1=d && c1=k}: x[a,b,c,d,e,f,j,k] <= Disp[d1,j];*/
 
 /* Separa as disciplinas por semestre, curso e período*/
 
 R1{p in periodo, C in cursos, s in semestres, j in diasN, k in hor}: sum{(a,b,c,d,e,f) in disciplinas:p=d && e=s && c=C} x[a,b,c,d,e,f,j,k] <= 1;
 
 /* Não alocar disciplinas de um mesmo professor no mesmo horário*/
 
 R2{p in periodo, j in diasN,l in professores, k in hor}: sum{(a,b,c,d,e,f) in disciplinas:b=l && d=p} x[a,b,c,d,e,f,j,k] <= 1;
 
 /* Cumprir ch semanal de cada disciplina */
 
 R3{(a,b,c,d,e,f) in disciplinas}:sum{j in diasN, k in hor} x[a,b,c,d,e,f,j,k] = 0.5*f;
 
 
 /* Alocar disciplinas de 4 aulas no mesmo dia */
 
 
R4{(a,b,c,d,e,f) in disciplinas, j in diasN:f=4}:x[a,b,c,d,e,f,j,1] - x[a,b,c,d,e,f,j,2] + x[a,b,c,d,e,f,j,3] = 0;
 
 
 
 
 /* Interstício */
 
 R5{j in 1..card(diasN)-2, p in professores, (a,b,c,d,e,f) in disciplinas, (A,B,C,D,E,F) in disciplinas:b=p && B=p && d="Noite" && D="Manhã"}: x[a,b,c,d,e,f,elemN[j],2] + x[A,B,C,D,E,F,elemN[j+1],1] <= 1;
 
 R6{p in professores, (a,b,c,d,e,f) in disciplinas:b=p && d="Noite"}:x[a,b,c,d,e,f,"sex",2] + x[a,b,c,d,e,f,"sab",1] <= 1;
 
 
 /* Máximo de 8 horas diárias de trabalho */
 

 
R7{j in diasN, p in professores, (a,b,c,d,e,f) in disciplinas:b=p}: sum {P in  periodo, k in hor:d=P} x[a,b,c,P,e,f,j,k] <= 4;


 /* Para printar o resultado */
 
 R8{C in cursos, P in periodo}:sum{k in hor, (a,b,c,d,e,f) in disciplinas:c=C && d=P}x[a,b,c,d,e,f,"seg",k]<=10000*print[C,P];
 
 R9{C in cursos, P in periodo, (a,b,c,d,e,f) in disciplinas:c=C && d=P}:sem[C,P]>=e;


/* terceiro horário noturno durante a semana não é permitido */

R10{j in diasN, (a,b,c,d,e,f) in disciplinas:j!="sab" && d="Noite"}:x[a,b,c,d,e,f,j,3]=0;


/* não alocar disciplinas aos sábados para cursos manhã e tarde */

R11{k in hor, (a,b,c,d,e,f) in disciplinas:d!="Noite"}: x[a,b,c,d,e,f,"sab",k]=0;



/* verificar infactibilidade de disponibilidade */




/*R10{}*/


 solve;
 
param exc:=sum{(a,b,c,d,e,f) in disciplinas,k in hor:d="Noite"} x[a,b,c,d,e,f,"sab",k] + sum{(a,b,c,d,e,f) in disciplinas, j in diasN:d!="Noite"} x[a,b,c,d,e,f,j,3]; 

/*param alocado:=total2+exc;*/


param alocado:= 2*sum{(a,b,c,d,e,f) in disciplinas,(a1,b1,c1,d1) in disp_cod, k in hor, j in diasN:a1=b && b1=d && c1=k && x[a,b,c,d,e,f,j,k]*Disp[d1,j]} x[a,b,c,d,e,f,j,k];



 
 /*-----------------------------------------------------------------------------
                Apresentação    do    Resultado     
------------------------------------------------------------------------------*/
 
 
 display ideal;
 
 display alocado;
 
 
printf "Horário Fatec v 1.1\n" > txt; 

printf "Alocação ideal  %d\n",ideal>>txt;

printf "Total alocado  %d\n",alocado>>txt;

for {{0}: ideal-alocado>0}{ printf "Disciplinas fora da disponibilidade dada\n">> txt;

for{(a,b,c,d,e,f) in disciplinas,(a1,b1,c1,d1) in disp_cod, k in hor, j in diasN:a1=b && b1=d && c1=k && x[a,b,c,d,e,f,j,k]=1 && Disp[d1,j]=0} printf "%s %s %s %s %d %s\n",c,d,a,j,k,b>> txt;        # IF condition THEN
} for {{0}: ideal-alocado<=0} { printf "\n">> txt; # ELSE
}   

 

/*printf "Disciplinas fora da disponibilidade dada\n">>txt;

for{(a,b,c,d,e,f) in disciplinas,(a1,b1,c1,d1) in disp_cod, k in hor, j in diasN:a1=b && b1=d && c1=k && x[a,b,c,d,e,f,j,k]=1 && Disp[d1,j]=0} printf "%s %s %s %s %d %s\n",c,d,a,j,k,b >> txt;*/


for{C in cursos, P in periodo, s in semestres:print[C,P]=1 && s<=sem[C,P]}
          {printf "\n\n%5s   %5s   Semestre %d\n\n",C, P, s >> txt; 
                for{j in diasN, k in hor,(a,b,c,d,e,f) in disciplinas:c=C && P=d && s=e && x[a,b,c,d,e,f,j,k]=1} printf "%5s;%5d;%15s;%15s;\n",j, k, a, b >> txt;}


/*printf "Horário Fatec v 1.0" > txt2; 

 for{C in cursos, P in periodo, s in semestres:print[C,P]=1 && s<=sem[C,P]}{printf "\n\n%s   %s   Semestre %d\n",C, P, s >> txt2;
    printf "%20s%20s%20s%20s%20s%20s\n","Segunda","Terça","Quarta","Quinta","Sexta","Sábado">>txt2;
    for{k in hor}{
      for{j in diasN}
        for{(a,b,c,d,e,f)in disciplinas:c=C && P=d && s=e && x[a,b,c,d,e,f,j,k]=1} 
          printf "%20s",a>>txt2;printf " \n">>txt2; }} */




printf "Horário Fatec v 1.1\n" > txt3; 

printf "Alocação ideal  %d\n",ideal>>txt3;

printf "Total alocado  %d\n",alocado>>txt3;

for {{0}: ideal-alocado>0}{ printf "Disciplinas fora da disponibilidade dada\n">> txt3;

for{(a,b,c,d,e,f) in disciplinas,(a1,b1,c1,d1) in disp_cod, k in hor, j in diasN:a1=b && b1=d && c1=k && x[a,b,c,d,e,f,j,k]=1 && Disp[d1,j]=0} printf "%s %s %s %s %d %s\n",c,d,a,j,k,b>> txt3;        # IF condition THEN
} for {{0}: ideal-alocado<=0} { printf "\n">> txt3; # ELSE
}   

 for{C in cursos, P in periodo, s in semestres:print[C,P]=1 && s<=sem[C,P]}{printf "\n\n%s   %s   Semestre %d\n",C, P, s >> txt3;
    printf "%20s%20s%20s%20s%20s%20s\n","Segunda","Terça","Quarta","Quinta","Sexta","Sábado">>txt3;
    for{k in hor}{
      for{j in diasN}{
           for{{0}:sum{(a,b,c,d,e,f)in disciplinas:c=C && P=d && s=e}x[a,b,c,d,e,f,j,k]=1}{for{(a,b,c,d,e,f)in disciplinas:c=C && P=d && s=e && x[a,b,c,d,e,f,j,k]=1}printf "%20s",a>>txt3;   /*printf"%20s","ok">>txt3;*/}
           for{{0}:sum{(a,b,c,d,e,f)in disciplinas:c=C && P=d && s=e}x[a,b,c,d,e,f,j,k]!=1}{printf"%20s","---">>txt3;
           
           
           
           
           
           }
        
        
        }
        printf"\n">>txt3;}
     
          
          printf " \n">>txt3; }



/*------------------------------------------------------------------------------
                         Dados       Complementares        
------------------------------------------------------------------------------*/



data;



param elemN [1] seg, [2] ter, [3] qua, [4] qui, [5] sex, [6] sab;
#param elemM [1] seg, [2] ter, [3] qua, [4] qui, [5] sex;

param T:=3;
param S:=6;




end;
