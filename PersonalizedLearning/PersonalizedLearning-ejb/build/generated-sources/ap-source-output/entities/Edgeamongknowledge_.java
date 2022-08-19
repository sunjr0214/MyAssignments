package entities;

import entities.Knowledge;
import entities.Learningresource;
import entities.Predicate;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:13")
@StaticMetamodel(Edgeamongknowledge.class)
public class Edgeamongknowledge_ { 

    public static volatile SingularAttribute<Edgeamongknowledge, Predicate> predicate;
    public static volatile SingularAttribute<Edgeamongknowledge, Knowledge> successornode;
    public static volatile SingularAttribute<Edgeamongknowledge, Integer> weight;
    public static volatile SingularAttribute<Edgeamongknowledge, String> memo;
    public static volatile SetAttribute<Edgeamongknowledge, Learningresource> learningresourceSet;
    public static volatile SingularAttribute<Edgeamongknowledge, Knowledge> predecessornode;
    public static volatile SingularAttribute<Edgeamongknowledge, Integer> id;

}