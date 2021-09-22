## Arithmetic	

- add immediate	addi RT,RA,SI
- add	add RT,RA,RB
- subtract	subf RT,RA,RB

## Data transfer	
- Load doubleword	ld RT,DS(RA)
- Store doubleword	std RS,DS(RA)
- Load word	lwz RT,D(RA)
- Store word	stw RS,D(RA)
- Load halfword	lhz RT,D(RA)
- Store halfword	sth RS,D(RA)
- Load byte	lbz RT,D(RA)
- Store byte	stb RS,D(RA)

## Logical	
- And	and RA RS RB
- Exclusive or	xor RA RS RB
- And immediate	andi RA,RS,UI
- Exclusive or immediate	xori RA,RS,UI

## Shift	
- Shift left logical	sld RA, RS, RB 
- Shift right logical	srd RA, RS, RB
- Shift right arithmetic	srad RA, RS, RB

## Unconditional branch	
- Unconditional Jump and link	
      - b LI (AA=0 LK=0) 
      - ba LI (AA=1 LK=0) 
      - bl LI (AA=0 LK=1) 
      - bla LI (AA=1 LK=1)

## Conditional branch	
- Branch conditional 
      - bc BO,BI,target_addr (AA=0 LK=0)
      - bca BO,BI,target_addr (AA=1 LK=0)
      - bcl BO,BI,target_addr (AA=0 LK=1)
      - bcla BO,BI,target_addr (AA=1 LK=1)


NB: This is a reduced instruction set. More instruction support will be added. So will memory addresses be expanded. 
