RawQuery = Struct.new(:class, :stmt, :from_scope, :caller_class_lst, :method_name, :filename, :line)

MetaQuery = Struct.new(:raw_query, :methods, :base_object_type,
                        :filters, :has_distinct, :has_limit)

Constr = Struct.new(:table, :type, :fields, :exists_in_db, :source)

QueryPredicate = Struct.new(:lh, :cmp, :rh, :ruby_meth)
QueryColumn = Struct.new(:table, :column, :ruby_meth)
MetaQuery2 = Struct.new(:raw_query, :has_distinct, :has_limit, :fields, :sql, :source, :methods, :components, :table)
QueryComponent = Struct.new(:meth, :param)
#QueryComponent = Struct.new(:table, :arg, :ruby_meth)

TableSchema = Struct.new(:class_name, :fields, :associations)

FileOutput = Struct.new(:file, :issues) do
    def to_s
        c = {}
        c["file"] = self[:file]
        c["issues"] = self[:issues].map{|issue| issue.to_s}
        return c.to_h
    end
end
Issue = Struct.new(:reason, :patch, :position) do 
    def to_s
        c = {}
        for m in self.members
            c[m] = self[m].to_s
        end
        return c.to_h
    end
end
Reason = Struct.new(:type, :detailed) do 
    def to_s
        self.to_h
    end
end
Position = Struct.new(:start, :end) do 
    def to_s
        c = {}
        for m in self.members
            c[m] = self[m].to_h
        end
        return c.to_h
    end
end
Point = Struct.new(:line, :column)
#association includes (:rel, :class_name, :field)
