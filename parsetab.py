
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEASSIGN BREAK CASE CHAR COLON COMMA DECREMENT DEFAULT DIVIDE DIVIDE_ASSIGN DOUBLE ELSE EQUAL FLOAT FOR GREATER_EQUAL GREATER_THAN IDENTIFIER IF INCREMENT INT LEFT_BRACE LEFT_PAREN LESS_EQUAL LESS_THAN MINUS MINUS_ASSIGN MULTIPLY MULTIPLY_ASSIGN NOT_EQUAL NUMBER PLUS PLUS_ASSIGN RIGHT_BRACE RIGHT_PAREN SEMICOLON SWITCH WHILEprogram : decl_var_list stmt_listdecl_var_list : decl_var_list decl_var\n                     | emptydecl_var : type id_list SEMICOLONtype : INT\n            | FLOAT\n            | DOUBLE\n            | CHARid_list : id_list COMMA IDENTIFIER\n               | IDENTIFIERstmt_list : stmt_list stmt\n                 | emptystmt : if_stmt\n            | switch_stmt\n            | while_stmt\n            | for_stmt\n            | assign_expr SEMICOLONif_stmt : IF LEFT_PAREN condition RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE else_partelse_part : ELSE LEFT_BRACE stmt_list RIGHT_BRACE\n                 | emptyswitch_stmt : SWITCH LEFT_PAREN IDENTIFIER RIGHT_PAREN LEFT_BRACE case_list default_part RIGHT_BRACEcase_list : case_list case_item\n                 | emptycase_item : CASE NUMBER COLON stmt_list BREAK SEMICOLON\n                 | CASE NUMBER COLON stmt_listdefault_part : DEFAULT COLON stmt_list\n                    | emptywhile_stmt : WHILE LEFT_PAREN condition RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACEfor_stmt : FOR LEFT_PAREN assign_expr SEMICOLON condition SEMICOLON assign_expr RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACEassign_expr : IDENTIFIER ASSIGN expr\n                   | IDENTIFIER PLUS_ASSIGN expr\n                   | IDENTIFIER MINUS_ASSIGN expr\n                   | IDENTIFIER MULTIPLY_ASSIGN expr\n                   | IDENTIFIER DIVIDE_ASSIGN expr\n                   | IDENTIFIER INCREMENT\n                   | IDENTIFIER DECREMENTexpr : expr PLUS expr\n            | expr MINUS expr\n            | expr MULTIPLY expr\n            | expr DIVIDE expr\n            | LEFT_PAREN expr RIGHT_PAREN\n            | NUMBER\n            | IDENTIFIERcondition : expr relational_operator exprrelational_operator : EQUAL\n                           | NOT_EQUAL\n                           | LESS_EQUAL\n                           | GREATER_EQUAL\n                           | LESS_THAN\n                           | GREATER_THANempty :'
    
_lr_action_items = {'INT':([0,2,3,5,37,],[-51,8,-3,-2,-4,]),'FLOAT':([0,2,3,5,37,],[-51,9,-3,-2,-4,]),'DOUBLE':([0,2,3,5,37,],[-51,10,-3,-2,-4,]),'CHAR':([0,2,3,5,37,],[-51,11,-3,-2,-4,]),'IF':([0,2,3,4,5,6,12,13,14,15,16,25,37,70,77,79,82,84,90,92,94,95,96,99,100,101,102,103,104,105,106,108,],[-51,-51,-3,18,-2,-12,-11,-13,-14,-15,-16,-17,-4,-51,-51,18,18,-51,-28,-18,-20,-21,-51,-51,18,-51,-51,18,18,18,-19,-29,]),'SWITCH':([0,2,3,4,5,6,12,13,14,15,16,25,37,70,77,79,82,84,90,92,94,95,96,99,100,101,102,103,104,105,106,108,],[-51,-51,-3,19,-2,-12,-11,-13,-14,-15,-16,-17,-4,-51,-51,19,19,-51,-28,-18,-20,-21,-51,-51,19,-51,-51,19,19,19,-19,-29,]),'WHILE':([0,2,3,4,5,6,12,13,14,15,16,25,37,70,77,79,82,84,90,92,94,95,96,99,100,101,102,103,104,105,106,108,],[-51,-51,-3,21,-2,-12,-11,-13,-14,-15,-16,-17,-4,-51,-51,21,21,-51,-28,-18,-20,-21,-51,-51,21,-51,-51,21,21,21,-19,-29,]),'FOR':([0,2,3,4,5,6,12,13,14,15,16,25,37,70,77,79,82,84,90,92,94,95,96,99,100,101,102,103,104,105,106,108,],[-51,-51,-3,22,-2,-12,-11,-13,-14,-15,-16,-17,-4,-51,-51,22,22,-51,-28,-18,-20,-21,-51,-51,22,-51,-51,22,22,22,-19,-29,]),'IDENTIFIER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,25,26,27,28,29,30,31,32,35,36,37,38,39,55,56,57,58,59,60,61,62,63,64,65,68,70,77,79,82,83,84,90,92,94,95,96,99,100,101,102,103,104,105,106,108,],[-51,-51,-3,20,-2,-12,24,-5,-6,-7,-8,-11,-13,-14,-15,-16,-17,43,44,43,43,43,43,43,43,20,-4,52,43,43,43,43,43,43,-45,-46,-47,-48,-49,-50,43,-51,-51,20,20,20,-51,-28,-18,-20,-21,-51,-51,20,-51,-51,20,20,20,-19,-29,]),'$end':([0,1,2,3,4,5,6,12,13,14,15,16,25,37,84,90,92,94,95,106,108,],[-51,0,-51,-3,-1,-2,-12,-11,-13,-14,-15,-16,-17,-4,-51,-28,-18,-20,-21,-19,-29,]),'RIGHT_BRACE':([6,12,13,14,15,16,25,70,76,77,79,80,81,82,84,85,86,88,90,92,94,95,96,99,100,101,102,103,104,105,106,108,109,],[-12,-11,-13,-14,-15,-16,-17,-51,-51,-51,84,-51,-23,90,-51,95,-22,-27,-28,-18,-20,-21,-51,-51,-26,-51,-51,106,-25,108,-19,-29,-24,]),'BREAK':([6,12,13,14,15,16,25,84,90,92,94,95,101,104,106,108,],[-12,-11,-13,-14,-15,-16,-17,-51,-28,-18,-20,-21,-51,107,-19,-29,]),'DEFAULT':([6,12,13,14,15,16,25,76,80,81,84,86,90,92,94,95,101,104,106,108,109,],[-12,-11,-13,-14,-15,-16,-17,-51,87,-23,-51,-22,-28,-18,-20,-21,-51,-25,-19,-29,-24,]),'CASE':([6,12,13,14,15,16,25,76,80,81,84,86,90,92,94,95,101,104,106,108,109,],[-12,-11,-13,-14,-15,-16,-17,-51,89,-23,-51,-22,-28,-18,-20,-21,-51,-25,-19,-29,-24,]),'SEMICOLON':([17,23,24,33,34,42,43,45,46,47,48,49,51,52,69,71,72,73,74,75,78,107,],[25,37,-10,-35,-36,-42,-43,-30,-31,-32,-33,-34,68,-9,-41,-44,-37,-38,-39,-40,83,109,]),'LEFT_PAREN':([18,19,21,22,26,28,29,30,31,32,35,39,55,56,57,58,59,60,61,62,63,64,65,68,],[26,27,35,36,39,39,39,39,39,39,39,39,39,39,39,39,39,-45,-46,-47,-48,-49,-50,39,]),'ASSIGN':([20,],[28,]),'PLUS_ASSIGN':([20,],[29,]),'MINUS_ASSIGN':([20,],[30,]),'MULTIPLY_ASSIGN':([20,],[31,]),'DIVIDE_ASSIGN':([20,],[32,]),'INCREMENT':([20,],[33,]),'DECREMENT':([20,],[34,]),'COMMA':([23,24,52,],[38,-10,-9,]),'NUMBER':([26,28,29,30,31,32,35,39,55,56,57,58,59,60,61,62,63,64,65,68,89,],[42,42,42,42,42,42,42,42,42,42,42,42,42,-45,-46,-47,-48,-49,-50,42,97,]),'RIGHT_PAREN':([33,34,40,42,43,44,45,46,47,48,49,50,53,69,71,72,73,74,75,91,],[-35,-36,54,-42,-43,66,-30,-31,-32,-33,-34,67,69,-41,-44,-37,-38,-39,-40,98,]),'PLUS':([41,42,43,45,46,47,48,49,53,69,71,72,73,74,75,],[56,-42,-43,56,56,56,56,56,56,-41,56,-37,-38,-39,-40,]),'MINUS':([41,42,43,45,46,47,48,49,53,69,71,72,73,74,75,],[57,-42,-43,57,57,57,57,57,57,-41,57,-37,-38,-39,-40,]),'MULTIPLY':([41,42,43,45,46,47,48,49,53,69,71,72,73,74,75,],[58,-42,-43,58,58,58,58,58,58,-41,58,58,58,-39,-40,]),'DIVIDE':([41,42,43,45,46,47,48,49,53,69,71,72,73,74,75,],[59,-42,-43,59,59,59,59,59,59,-41,59,59,59,-39,-40,]),'EQUAL':([41,42,43,69,72,73,74,75,],[60,-42,-43,-41,-37,-38,-39,-40,]),'NOT_EQUAL':([41,42,43,69,72,73,74,75,],[61,-42,-43,-41,-37,-38,-39,-40,]),'LESS_EQUAL':([41,42,43,69,72,73,74,75,],[62,-42,-43,-41,-37,-38,-39,-40,]),'GREATER_EQUAL':([41,42,43,69,72,73,74,75,],[63,-42,-43,-41,-37,-38,-39,-40,]),'LESS_THAN':([41,42,43,69,72,73,74,75,],[64,-42,-43,-41,-37,-38,-39,-40,]),'GREATER_THAN':([41,42,43,69,72,73,74,75,],[65,-42,-43,-41,-37,-38,-39,-40,]),'LEFT_BRACE':([54,66,67,93,98,],[70,76,77,99,102,]),'ELSE':([84,],[93,]),'COLON':([87,97,],[96,101,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'decl_var_list':([0,],[2,]),'empty':([0,2,70,76,77,80,84,96,99,101,102,],[3,6,6,81,6,88,94,6,6,6,6,]),'stmt_list':([2,70,77,96,99,101,102,],[4,79,82,100,103,104,105,]),'decl_var':([2,],[5,]),'type':([2,],[7,]),'stmt':([4,79,82,100,103,104,105,],[12,12,12,12,12,12,12,]),'if_stmt':([4,79,82,100,103,104,105,],[13,13,13,13,13,13,13,]),'switch_stmt':([4,79,82,100,103,104,105,],[14,14,14,14,14,14,14,]),'while_stmt':([4,79,82,100,103,104,105,],[15,15,15,15,15,15,15,]),'for_stmt':([4,79,82,100,103,104,105,],[16,16,16,16,16,16,16,]),'assign_expr':([4,36,79,82,83,100,103,104,105,],[17,51,17,17,91,17,17,17,17,]),'id_list':([7,],[23,]),'condition':([26,35,68,],[40,50,78,]),'expr':([26,28,29,30,31,32,35,39,55,56,57,58,59,68,],[41,45,46,47,48,49,41,53,71,72,73,74,75,41,]),'relational_operator':([41,],[55,]),'case_list':([76,],[80,]),'default_part':([80,],[85,]),'case_item':([80,],[86,]),'else_part':([84,],[92,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> decl_var_list stmt_list','program',2,'p_program','parser.py',15),
  ('decl_var_list -> decl_var_list decl_var','decl_var_list',2,'p_decl_var_list','parser.py',19),
  ('decl_var_list -> empty','decl_var_list',1,'p_decl_var_list','parser.py',20),
  ('decl_var -> type id_list SEMICOLON','decl_var',3,'p_decl_var','parser.py',24),
  ('type -> INT','type',1,'p_type','parser.py',28),
  ('type -> FLOAT','type',1,'p_type','parser.py',29),
  ('type -> DOUBLE','type',1,'p_type','parser.py',30),
  ('type -> CHAR','type',1,'p_type','parser.py',31),
  ('id_list -> id_list COMMA IDENTIFIER','id_list',3,'p_id_list','parser.py',35),
  ('id_list -> IDENTIFIER','id_list',1,'p_id_list','parser.py',36),
  ('stmt_list -> stmt_list stmt','stmt_list',2,'p_stmt_list','parser.py',40),
  ('stmt_list -> empty','stmt_list',1,'p_stmt_list','parser.py',41),
  ('stmt -> if_stmt','stmt',1,'p_stmt','parser.py',45),
  ('stmt -> switch_stmt','stmt',1,'p_stmt','parser.py',46),
  ('stmt -> while_stmt','stmt',1,'p_stmt','parser.py',47),
  ('stmt -> for_stmt','stmt',1,'p_stmt','parser.py',48),
  ('stmt -> assign_expr SEMICOLON','stmt',2,'p_stmt','parser.py',49),
  ('if_stmt -> IF LEFT_PAREN condition RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE else_part','if_stmt',8,'p_if_stmt','parser.py',53),
  ('else_part -> ELSE LEFT_BRACE stmt_list RIGHT_BRACE','else_part',4,'p_else_part','parser.py',57),
  ('else_part -> empty','else_part',1,'p_else_part','parser.py',58),
  ('switch_stmt -> SWITCH LEFT_PAREN IDENTIFIER RIGHT_PAREN LEFT_BRACE case_list default_part RIGHT_BRACE','switch_stmt',8,'p_switch_stmt','parser.py',62),
  ('case_list -> case_list case_item','case_list',2,'p_case_list','parser.py',66),
  ('case_list -> empty','case_list',1,'p_case_list','parser.py',67),
  ('case_item -> CASE NUMBER COLON stmt_list BREAK SEMICOLON','case_item',6,'p_case_item','parser.py',71),
  ('case_item -> CASE NUMBER COLON stmt_list','case_item',4,'p_case_item','parser.py',72),
  ('default_part -> DEFAULT COLON stmt_list','default_part',3,'p_default_part','parser.py',76),
  ('default_part -> empty','default_part',1,'p_default_part','parser.py',77),
  ('while_stmt -> WHILE LEFT_PAREN condition RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE','while_stmt',7,'p_while_stmt','parser.py',81),
  ('for_stmt -> FOR LEFT_PAREN assign_expr SEMICOLON condition SEMICOLON assign_expr RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE','for_stmt',11,'p_for_stmt','parser.py',85),
  ('assign_expr -> IDENTIFIER ASSIGN expr','assign_expr',3,'p_assign_expr','parser.py',89),
  ('assign_expr -> IDENTIFIER PLUS_ASSIGN expr','assign_expr',3,'p_assign_expr','parser.py',90),
  ('assign_expr -> IDENTIFIER MINUS_ASSIGN expr','assign_expr',3,'p_assign_expr','parser.py',91),
  ('assign_expr -> IDENTIFIER MULTIPLY_ASSIGN expr','assign_expr',3,'p_assign_expr','parser.py',92),
  ('assign_expr -> IDENTIFIER DIVIDE_ASSIGN expr','assign_expr',3,'p_assign_expr','parser.py',93),
  ('assign_expr -> IDENTIFIER INCREMENT','assign_expr',2,'p_assign_expr','parser.py',94),
  ('assign_expr -> IDENTIFIER DECREMENT','assign_expr',2,'p_assign_expr','parser.py',95),
  ('expr -> expr PLUS expr','expr',3,'p_expr','parser.py',99),
  ('expr -> expr MINUS expr','expr',3,'p_expr','parser.py',100),
  ('expr -> expr MULTIPLY expr','expr',3,'p_expr','parser.py',101),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr','parser.py',102),
  ('expr -> LEFT_PAREN expr RIGHT_PAREN','expr',3,'p_expr','parser.py',103),
  ('expr -> NUMBER','expr',1,'p_expr','parser.py',104),
  ('expr -> IDENTIFIER','expr',1,'p_expr','parser.py',105),
  ('condition -> expr relational_operator expr','condition',3,'p_condition','parser.py',109),
  ('relational_operator -> EQUAL','relational_operator',1,'p_relational_operator','parser.py',113),
  ('relational_operator -> NOT_EQUAL','relational_operator',1,'p_relational_operator','parser.py',114),
  ('relational_operator -> LESS_EQUAL','relational_operator',1,'p_relational_operator','parser.py',115),
  ('relational_operator -> GREATER_EQUAL','relational_operator',1,'p_relational_operator','parser.py',116),
  ('relational_operator -> LESS_THAN','relational_operator',1,'p_relational_operator','parser.py',117),
  ('relational_operator -> GREATER_THAN','relational_operator',1,'p_relational_operator','parser.py',118),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',122),
]
