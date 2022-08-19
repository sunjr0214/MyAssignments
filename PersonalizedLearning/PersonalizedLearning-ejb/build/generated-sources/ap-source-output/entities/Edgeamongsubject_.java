package entities;

import entities.Predicate;
import entities.Subject;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-19T11:48:14")
@StaticMetamodel(Edgeamongsubject.class)
public class Edgeamongsubject_ { 

    public static volatile SingularAttribute<Edgeamongsubject, Predicate> predicate;
    public static volatile SingularAttribute<Edgeamongsubject, Subject> successornode;
    public static volatile SingularAttribute<Edgeamongsubject, Integer> weight;
    public static volatile SingularAttribute<Edgeamongsubject, String> memo;
    public static volatile SingularAttribute<Edgeamongsubject, Subject> predecessornode;
    public static volatile SingularAttribute<Edgeamongsubject, Integer> id;

}