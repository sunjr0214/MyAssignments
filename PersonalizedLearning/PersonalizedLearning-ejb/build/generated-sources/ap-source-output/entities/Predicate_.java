package entities;

import entities.Edgeamongknowledge;
import entities.Edgeamongsubject;
import javax.annotation.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.5.2.v20140319-rNA", date="2022-08-18T21:55:03")
@StaticMetamodel(Predicate.class)
public class Predicate_ { 

    public static volatile SingularAttribute<Predicate, String> colorname;
    public static volatile SingularAttribute<Predicate, Boolean> symmetry;
    public static volatile SingularAttribute<Predicate, String> pname;
    public static volatile SingularAttribute<Predicate, String> meaning;
    public static volatile SingularAttribute<Predicate, Boolean> transitivity;
    public static volatile SetAttribute<Predicate, Edgeamongsubject> edgeamongsubjectSet;
    public static volatile SingularAttribute<Predicate, String> memo;
    public static volatile SingularAttribute<Predicate, Integer> id;
    public static volatile SingularAttribute<Predicate, Boolean> reflexivity;
    public static volatile SingularAttribute<Predicate, Integer> porder;
    public static volatile SingularAttribute<Predicate, String> myalias;
    public static volatile SetAttribute<Predicate, Edgeamongknowledge> edgeamongknowledgeSet;

}