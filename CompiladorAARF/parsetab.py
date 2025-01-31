
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'B_DERECHO B_IZQUIERDO COMA CTE_FLOAT CTE_INT CTE_STRING DIFE DIV DO ELSE END ENTERO FLOTANTE ID IF IGUAL K_DERECHO K_IZQUIERDO MAIN MAYOR MENOR MULT PRINT PROGRAMA P_COMA P_DERECHO P_IZQUIERDO P_PUNTO RESTA SUMA VARIABLE VOID WHILEprogram : PROGRAMA ID pn1 P_COMA dec_Vars dec1_F MAIN Body ENDdec_Vars : Vars \n                | epsilondec1_F : Funcs dec1_F \n              | epsilonpn1 : Vars : VARIABLE mas_Varsmas_Vars : id_Vars P_PUNTO Type pn2 P_COMA rep_Varsid_Vars : ID pn3 mas_idmas_id : COMA id_Vars \n              | epsilonrep_Vars : mas_Vars \n                | epsilonpn2 : pn3 : Body : K_IZQUIERDO dec_State K_DERECHOdec_State : Statement dec_State \n                 | epsilonStatement : Assign \n                 | Condition \n                 | Cycle \n                 | F_Call \n                 | PrintPrint : PRINT P_IZQUIERDO dec_Expresion P_DERECHO P_COMAdec_Expresion : Expresion pn2p mas_Print\n                     | CTE_STRING  pn1p mas_Printmas_Print : COMA dec_Expresion \n                 | epsilonpn1p : pn2p : Cycle : DO pn1c Body WHILE P_IZQUIERDO Expresion pn2c P_DERECHO P_COMApn1c : pn2c : Condition : IF P_IZQUIERDO Expresion pn1i P_DERECHO Body mas_if P_COMA pn2i mas_if : ELSE pn3i Body \n              | epsilonpn1i : pn2i : pn3i : Assign : ID pn1a IGUAL pn2a Expresion pn3a P_COMApn1a : pn2a : pn3a : Expresion : EXP mas_Emas_E : operators pn8e EXP pn9e\n             | epsilonoperators : MAYOR  \n                 | MENOR \n                 | DIFEEXP : Termino pn4e mas_EXPmas_EXP : SUMA pn3e EXP \n               | RESTA  pn3e EXP \n               | epsilonpn3e : pn4e : pn8e : pn9e : Termino : Factor pn5e mas_Termmas_Term : MULT pn2e Termino \n                | DIV pn2e Termino \n                | epsilonpn2e : pn5e : Factor : P_IZQUIERDO pn6e Expresion pn7e P_DERECHO \n              | dec_Factor mas_Factor dec_Factor : SUMA \n                  | RESTA \n                  | epsilonmas_Factor : ID pn1e\n                  | CTE pn1e2pn1e : pn1e2 : pn6e : pn7e : CTE : CTE_FLOAT pnAux\n           | CTE_INT pnAux2pnAux : pnAux2 : Funcs : VOID ID pn4 P_IZQUIERDO mas_Func P_DERECHO B_IZQUIERDO dec_Vars Body pn6 B_DERECHO P_COMAmas_Func : ID P_PUNTO Type pn5 mas2_Func\n                | epsilon mas2_Func : COMA mas_Func \n                 | epsilonpn4 : pn5 : pn6 : F_Call : ID P_IZQUIERDO mas_F P_DERECHO P_COMAmas_F : Expresion mas2_F \n             | epsilonmas2_F : COMA mas_F \n              | epsilonType : ENTERO \n            | FLOTANTEepsilon : '
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,31,],[0,-1,]),'ID':([2,9,13,23,29,33,35,36,37,38,39,44,50,51,53,57,58,59,62,66,67,68,70,80,81,84,87,89,90,91,108,110,112,113,116,117,124,125,127,135,136,137,138,143,146,159,163,165,],[3,16,19,40,16,40,-19,-20,-21,-22,-23,54,-94,-94,-94,16,-42,-73,-68,95,-66,-67,-68,-94,-94,-94,-56,-47,-48,-49,-87,-94,-54,-54,-62,-62,-94,-24,-94,-94,-94,-94,-94,54,-40,-38,-34,-31,]),'P_COMA':([3,4,25,26,27,45,47,63,64,65,82,86,88,92,93,94,95,96,97,98,101,106,111,114,115,118,119,120,121,122,132,134,139,147,148,149,150,151,152,153,155,161,162,164,],[-6,5,-14,-92,-93,57,-16,-94,-55,-63,108,-44,-46,-94,-94,-65,-71,-72,-77,-78,125,-43,-50,-53,-58,-61,-69,-70,-75,-76,146,-57,-94,-64,-45,-51,-52,-59,-60,159,-36,165,166,-35,]),'VARIABLE':([5,105,],[9,9,]),'VOID':([5,6,7,8,11,14,57,77,78,79,166,],[-94,13,-2,-3,13,-7,-94,-8,-12,-13,-79,]),'MAIN':([5,6,7,8,10,11,12,14,18,57,77,78,79,166,],[-94,-94,-2,-3,17,-94,-5,-7,-4,-94,-8,-12,-13,-79,]),'K_IZQUIERDO':([7,8,14,17,42,52,57,77,78,79,105,123,131,154,160,],[-2,-3,-7,23,-32,23,-94,-8,-12,-13,-94,23,23,-39,23,]),'P_PUNTO':([15,16,21,28,30,46,54,],[20,-15,-94,-9,-11,-10,75,]),'COMA':([16,21,26,27,61,63,64,65,73,74,86,88,92,93,94,95,96,97,98,102,103,104,111,114,115,118,119,120,121,122,130,134,147,148,149,150,151,152,],[-15,29,-92,-93,84,-94,-55,-63,-30,-29,-44,-46,-94,-94,-65,-71,-72,-77,-78,127,127,-85,-50,-53,-58,-61,-69,-70,-75,-76,143,-57,-64,-45,-51,-52,-59,-60,]),'P_IZQUIERDO':([19,24,40,41,43,50,51,53,58,59,80,81,84,87,89,90,91,100,110,112,113,116,117,124,127,135,136,137,138,],[-84,44,50,51,53,59,59,59,-42,-73,59,59,59,-56,-47,-48,-49,124,59,-54,-54,-62,-62,59,59,59,59,59,59,]),'ENTERO':([20,75,],[26,26,]),'FLOTANTE':([20,75,],[27,27,]),'END':([22,47,],[31,-16,]),'K_DERECHO':([23,32,33,34,35,36,37,38,39,48,108,125,146,159,163,165,],[-94,47,-94,-18,-19,-20,-21,-22,-23,-17,-87,-24,-40,-38,-34,-31,]),'IF':([23,33,35,36,37,38,39,108,125,146,159,163,165,],[41,41,-19,-20,-21,-22,-23,-87,-24,-40,-38,-34,-31,]),'DO':([23,33,35,36,37,38,39,108,125,146,159,163,165,],[42,42,-19,-20,-21,-22,-23,-87,-24,-40,-38,-34,-31,]),'PRINT':([23,33,35,36,37,38,39,108,125,146,159,163,165,],[43,43,-19,-20,-21,-22,-23,-87,-24,-40,-38,-34,-31,]),'P_DERECHO':([26,27,44,50,55,56,60,61,62,63,64,65,69,72,73,74,83,84,85,86,88,92,93,94,95,96,97,98,99,102,103,104,107,109,111,114,115,118,119,120,121,122,126,128,129,130,133,134,140,141,142,143,144,147,148,149,150,151,152,156,157,],[-92,-93,-94,-94,76,-81,82,-94,-89,-94,-55,-63,-37,101,-30,-29,-88,-94,-91,-44,-46,-94,-94,-65,-71,-72,-77,-78,123,-94,-94,-85,-74,-90,-50,-53,-58,-61,-69,-70,-75,-76,-25,-28,-26,-94,147,-57,-33,-27,-80,-94,-83,-64,-45,-51,-52,-59,-60,161,-82,]),'IGUAL':([40,49,],[-41,58,]),'WHILE':([47,71,],[-16,100,]),'ELSE':([47,139,],[-16,154,]),'B_DERECHO':([47,145,158,],[-16,-86,162,]),'CTE_FLOAT':([50,51,53,58,59,62,66,67,68,70,80,81,84,87,89,90,91,110,112,113,116,117,124,127,135,136,137,138,],[-94,-94,-94,-42,-73,-68,97,-66,-67,-68,-94,-94,-94,-56,-47,-48,-49,-94,-54,-54,-62,-62,-94,-94,-94,-94,-94,-94,]),'CTE_INT':([50,51,53,58,59,62,66,67,68,70,80,81,84,87,89,90,91,110,112,113,116,117,124,127,135,136,137,138,],[-94,-94,-94,-42,-73,-68,98,-66,-67,-68,-94,-94,-94,-56,-47,-48,-49,-94,-54,-54,-62,-62,-94,-94,-94,-94,-94,-94,]),'SUMA':([50,51,53,58,59,64,65,80,81,84,87,89,90,91,92,93,94,95,96,97,98,110,112,113,115,116,117,118,119,120,121,122,124,127,135,136,137,138,147,151,152,],[67,67,67,-42,-73,-55,-63,67,67,67,-56,-47,-48,-49,112,-94,-65,-71,-72,-77,-78,67,-54,-54,-58,-62,-62,-61,-69,-70,-75,-76,67,67,67,67,67,67,-64,-59,-60,]),'RESTA':([50,51,53,58,59,64,65,80,81,84,87,89,90,91,92,93,94,95,96,97,98,110,112,113,115,116,117,118,119,120,121,122,124,127,135,136,137,138,147,151,152,],[68,68,68,-42,-73,-55,-63,68,68,68,-56,-47,-48,-49,113,-94,-65,-71,-72,-77,-78,68,-54,-54,-58,-62,-62,-61,-69,-70,-75,-76,68,68,68,68,68,68,-64,-59,-60,]),'CTE_STRING':([53,127,],[74,74,]),'MAYOR':([63,64,65,92,93,94,95,96,97,98,111,114,115,118,119,120,121,122,147,149,150,151,152,],[89,-55,-63,-94,-94,-65,-71,-72,-77,-78,-50,-53,-58,-61,-69,-70,-75,-76,-64,-51,-52,-59,-60,]),'MENOR':([63,64,65,92,93,94,95,96,97,98,111,114,115,118,119,120,121,122,147,149,150,151,152,],[90,-55,-63,-94,-94,-65,-71,-72,-77,-78,-50,-53,-58,-61,-69,-70,-75,-76,-64,-51,-52,-59,-60,]),'DIFE':([63,64,65,92,93,94,95,96,97,98,111,114,115,118,119,120,121,122,147,149,150,151,152,],[91,-55,-63,-94,-94,-65,-71,-72,-77,-78,-50,-53,-58,-61,-69,-70,-75,-76,-64,-51,-52,-59,-60,]),'MULT':([65,93,94,95,96,97,98,119,120,121,122,147,],[-63,116,-65,-71,-72,-77,-78,-69,-70,-75,-76,-64,]),'DIV':([65,93,94,95,96,97,98,119,120,121,122,147,],[-63,117,-65,-71,-72,-77,-78,-69,-70,-75,-76,-64,]),'B_IZQUIERDO':([76,],[105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'pn1':([3,],[4,]),'dec_Vars':([5,105,],[6,131,]),'Vars':([5,105,],[7,7,]),'epsilon':([5,6,11,21,23,33,44,50,51,53,57,61,63,80,81,84,92,93,102,103,105,110,124,127,130,135,136,137,138,139,143,],[8,12,12,30,34,34,56,62,70,70,79,85,88,70,70,62,114,118,128,128,8,70,70,70,144,70,70,70,70,155,56,]),'dec1_F':([6,11,],[10,18,]),'Funcs':([6,11,],[11,11,]),'mas_Vars':([9,57,],[14,78,]),'id_Vars':([9,29,57,],[15,46,15,]),'pn3':([16,],[21,]),'Body':([17,52,123,131,160,],[22,71,139,145,164,]),'pn4':([19,],[24,]),'Type':([20,75,],[25,104,]),'mas_id':([21,],[28,]),'dec_State':([23,33,],[32,48,]),'Statement':([23,33,],[33,33,]),'Assign':([23,33,],[35,35,]),'Condition':([23,33,],[36,36,]),'Cycle':([23,33,],[37,37,]),'F_Call':([23,33,],[38,38,]),'Print':([23,33,],[39,39,]),'pn2':([25,],[45,]),'pn1a':([40,],[49,]),'pn1c':([42,],[52,]),'mas_Func':([44,143,],[55,157,]),'mas_F':([50,84,],[60,109,]),'Expresion':([50,51,53,80,81,84,124,127,],[61,69,73,106,107,61,140,73,]),'EXP':([50,51,53,80,81,84,110,124,127,135,136,],[63,63,63,63,63,63,134,63,63,149,150,]),'Termino':([50,51,53,80,81,84,110,124,127,135,136,137,138,],[64,64,64,64,64,64,64,64,64,64,64,151,152,]),'Factor':([50,51,53,80,81,84,110,124,127,135,136,137,138,],[65,65,65,65,65,65,65,65,65,65,65,65,65,]),'dec_Factor':([50,51,53,80,81,84,110,124,127,135,136,137,138,],[66,66,66,66,66,66,66,66,66,66,66,66,66,]),'dec_Expresion':([53,127,],[72,141,]),'rep_Vars':([57,],[77,]),'pn2a':([58,],[80,]),'pn6e':([59,],[81,]),'mas2_F':([61,],[83,]),'mas_E':([63,],[86,]),'operators':([63,],[87,]),'pn4e':([64,],[92,]),'pn5e':([65,],[93,]),'mas_Factor':([66,],[94,]),'CTE':([66,],[96,]),'pn1i':([69,],[99,]),'pn2p':([73,],[102,]),'pn1p':([74,],[103,]),'pn8e':([87,],[110,]),'mas_EXP':([92,],[111,]),'mas_Term':([93,],[115,]),'pn1e':([95,],[119,]),'pn1e2':([96,],[120,]),'pnAux':([97,],[121,]),'pnAux2':([98,],[122,]),'mas_Print':([102,103,],[126,129,]),'pn5':([104,],[130,]),'pn3a':([106,],[132,]),'pn7e':([107,],[133,]),'pn3e':([112,113,],[135,136,]),'pn2e':([116,117,],[137,138,]),'mas2_Func':([130,],[142,]),'pn9e':([134,],[148,]),'mas_if':([139,],[153,]),'pn2c':([140,],[156,]),'pn6':([145,],[158,]),'pn3i':([154,],[160,]),'pn2i':([159,],[163,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAMA ID pn1 P_COMA dec_Vars dec1_F MAIN Body END','program',9,'p_program','sintactico.py',38),
  ('dec_Vars -> Vars','dec_Vars',1,'p_dec_Vars','sintactico.py',41),
  ('dec_Vars -> epsilon','dec_Vars',1,'p_dec_Vars','sintactico.py',42),
  ('dec1_F -> Funcs dec1_F','dec1_F',2,'p_dec1_F','sintactico.py',45),
  ('dec1_F -> epsilon','dec1_F',1,'p_dec1_F','sintactico.py',46),
  ('pn1 -> <empty>','pn1',0,'p_pn1','sintactico.py',50),
  ('Vars -> VARIABLE mas_Vars','Vars',2,'p_Vars','sintactico.py',60),
  ('mas_Vars -> id_Vars P_PUNTO Type pn2 P_COMA rep_Vars','mas_Vars',6,'p_mas_Vars','sintactico.py',63),
  ('id_Vars -> ID pn3 mas_id','id_Vars',3,'p_id_Vars','sintactico.py',66),
  ('mas_id -> COMA id_Vars','mas_id',2,'p_mas_id','sintactico.py',69),
  ('mas_id -> epsilon','mas_id',1,'p_mas_id','sintactico.py',70),
  ('rep_Vars -> mas_Vars','rep_Vars',1,'p_rep_Vars','sintactico.py',73),
  ('rep_Vars -> epsilon','rep_Vars',1,'p_rep_Vars','sintactico.py',74),
  ('pn2 -> <empty>','pn2',0,'p_pn2','sintactico.py',78),
  ('pn3 -> <empty>','pn3',0,'p_pn3','sintactico.py',86),
  ('Body -> K_IZQUIERDO dec_State K_DERECHO','Body',3,'p_Body','sintactico.py',93),
  ('dec_State -> Statement dec_State','dec_State',2,'p_dec_State','sintactico.py',96),
  ('dec_State -> epsilon','dec_State',1,'p_dec_State','sintactico.py',97),
  ('Statement -> Assign','Statement',1,'p_Statement','sintactico.py',103),
  ('Statement -> Condition','Statement',1,'p_Statement','sintactico.py',104),
  ('Statement -> Cycle','Statement',1,'p_Statement','sintactico.py',105),
  ('Statement -> F_Call','Statement',1,'p_Statement','sintactico.py',106),
  ('Statement -> Print','Statement',1,'p_Statement','sintactico.py',107),
  ('Print -> PRINT P_IZQUIERDO dec_Expresion P_DERECHO P_COMA','Print',5,'p_Print','sintactico.py',113),
  ('dec_Expresion -> Expresion pn2p mas_Print','dec_Expresion',3,'p_dec_Expresion','sintactico.py',116),
  ('dec_Expresion -> CTE_STRING pn1p mas_Print','dec_Expresion',3,'p_dec_Expresion','sintactico.py',117),
  ('mas_Print -> COMA dec_Expresion','mas_Print',2,'p_mas_Print','sintactico.py',120),
  ('mas_Print -> epsilon','mas_Print',1,'p_mas_Print','sintactico.py',121),
  ('pn1p -> <empty>','pn1p',0,'p_pn1p','sintactico.py',125),
  ('pn2p -> <empty>','pn2p',0,'p_pn2p','sintactico.py',130),
  ('Cycle -> DO pn1c Body WHILE P_IZQUIERDO Expresion pn2c P_DERECHO P_COMA','Cycle',9,'p_Cycle','sintactico.py',139),
  ('pn1c -> <empty>','pn1c',0,'p_pn1c','sintactico.py',143),
  ('pn2c -> <empty>','pn2c',0,'p_pn2c','sintactico.py',148),
  ('Condition -> IF P_IZQUIERDO Expresion pn1i P_DERECHO Body mas_if P_COMA pn2i','Condition',9,'p_Condition','sintactico.py',158),
  ('mas_if -> ELSE pn3i Body','mas_if',3,'p_mas_if','sintactico.py',161),
  ('mas_if -> epsilon','mas_if',1,'p_mas_if','sintactico.py',162),
  ('pn1i -> <empty>','pn1i',0,'p_pn1i','sintactico.py',166),
  ('pn2i -> <empty>','pn2i',0,'p_pn2i','sintactico.py',177),
  ('pn3i -> <empty>','pn3i',0,'p_pn3i','sintactico.py',183),
  ('Assign -> ID pn1a IGUAL pn2a Expresion pn3a P_COMA','Assign',7,'p_Assign','sintactico.py',193),
  ('pn1a -> <empty>','pn1a',0,'p_pn1a','sintactico.py',197),
  ('pn2a -> <empty>','pn2a',0,'p_pn2a','sintactico.py',204),
  ('pn3a -> <empty>','pn3a',0,'p_pn3a','sintactico.py',209),
  ('Expresion -> EXP mas_E','Expresion',2,'p_Expresion','sintactico.py',229),
  ('mas_E -> operators pn8e EXP pn9e','mas_E',4,'p_mas_E','sintactico.py',232),
  ('mas_E -> epsilon','mas_E',1,'p_mas_E','sintactico.py',233),
  ('operators -> MAYOR','operators',1,'p_operators','sintactico.py',236),
  ('operators -> MENOR','operators',1,'p_operators','sintactico.py',237),
  ('operators -> DIFE','operators',1,'p_operators','sintactico.py',238),
  ('EXP -> Termino pn4e mas_EXP','EXP',3,'p_EXP','sintactico.py',242),
  ('mas_EXP -> SUMA pn3e EXP','mas_EXP',3,'p_mas_EXP','sintactico.py',245),
  ('mas_EXP -> RESTA pn3e EXP','mas_EXP',3,'p_mas_EXP','sintactico.py',246),
  ('mas_EXP -> epsilon','mas_EXP',1,'p_mas_EXP','sintactico.py',247),
  ('pn3e -> <empty>','pn3e',0,'p_pn3e','sintactico.py',251),
  ('pn4e -> <empty>','pn4e',0,'p_pn4e','sintactico.py',256),
  ('pn8e -> <empty>','pn8e',0,'p_pn8e','sintactico.py',281),
  ('pn9e -> <empty>','pn9e',0,'p_pn9e','sintactico.py',286),
  ('Termino -> Factor pn5e mas_Term','Termino',3,'p_Termino','sintactico.py',312),
  ('mas_Term -> MULT pn2e Termino','mas_Term',3,'p_mas_Term','sintactico.py',315),
  ('mas_Term -> DIV pn2e Termino','mas_Term',3,'p_mas_Term','sintactico.py',316),
  ('mas_Term -> epsilon','mas_Term',1,'p_mas_Term','sintactico.py',317),
  ('pn2e -> <empty>','pn2e',0,'p_pn2e','sintactico.py',321),
  ('pn5e -> <empty>','pn5e',0,'p_pn5e','sintactico.py',326),
  ('Factor -> P_IZQUIERDO pn6e Expresion pn7e P_DERECHO','Factor',5,'p_Factor','sintactico.py',353),
  ('Factor -> dec_Factor mas_Factor','Factor',2,'p_Factor','sintactico.py',354),
  ('dec_Factor -> SUMA','dec_Factor',1,'p_dec_Factor','sintactico.py',357),
  ('dec_Factor -> RESTA','dec_Factor',1,'p_dec_Factor','sintactico.py',358),
  ('dec_Factor -> epsilon','dec_Factor',1,'p_dec_Factor','sintactico.py',359),
  ('mas_Factor -> ID pn1e','mas_Factor',2,'p_mas_Factor','sintactico.py',362),
  ('mas_Factor -> CTE pn1e2','mas_Factor',2,'p_mas_Factor','sintactico.py',363),
  ('pn1e -> <empty>','pn1e',0,'p_pn1e','sintactico.py',367),
  ('pn1e2 -> <empty>','pn1e2',0,'p_pn1e2','sintactico.py',374),
  ('pn6e -> <empty>','pn6e',0,'p_pn6e','sintactico.py',381),
  ('pn7e -> <empty>','pn7e',0,'p_pn7e','sintactico.py',386),
  ('CTE -> CTE_FLOAT pnAux','CTE',2,'p_CTE','sintactico.py',396),
  ('CTE -> CTE_INT pnAux2','CTE',2,'p_CTE','sintactico.py',397),
  ('pnAux -> <empty>','pnAux',0,'p_pnAux','sintactico.py',402),
  ('pnAux2 -> <empty>','pnAux2',0,'p_pnAux2','sintactico.py',407),
  ('Funcs -> VOID ID pn4 P_IZQUIERDO mas_Func P_DERECHO B_IZQUIERDO dec_Vars Body pn6 B_DERECHO P_COMA','Funcs',12,'p_Funcs','sintactico.py',414),
  ('mas_Func -> ID P_PUNTO Type pn5 mas2_Func','mas_Func',5,'p_mas_Func','sintactico.py',417),
  ('mas_Func -> epsilon','mas_Func',1,'p_mas_Func','sintactico.py',418),
  ('mas2_Func -> COMA mas_Func','mas2_Func',2,'p_mas2_Func','sintactico.py',421),
  ('mas2_Func -> epsilon','mas2_Func',1,'p_mas2_Func','sintactico.py',422),
  ('pn4 -> <empty>','pn4',0,'p_pn4','sintactico.py',426),
  ('pn5 -> <empty>','pn5',0,'p_pn5','sintactico.py',432),
  ('pn6 -> <empty>','pn6',0,'p_pn6','sintactico.py',437),
  ('F_Call -> ID P_IZQUIERDO mas_F P_DERECHO P_COMA','F_Call',5,'p_F_Call','sintactico.py',444),
  ('mas_F -> Expresion mas2_F','mas_F',2,'p_mas_F','sintactico.py',447),
  ('mas_F -> epsilon','mas_F',1,'p_mas_F','sintactico.py',448),
  ('mas2_F -> COMA mas_F','mas2_F',2,'p_mas2_F','sintactico.py',451),
  ('mas2_F -> epsilon','mas2_F',1,'p_mas2_F','sintactico.py',452),
  ('Type -> ENTERO','Type',1,'p_Type','sintactico.py',457),
  ('Type -> FLOTANTE','Type',1,'p_Type','sintactico.py',458),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','sintactico.py',462),
]
