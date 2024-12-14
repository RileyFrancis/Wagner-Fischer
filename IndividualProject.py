from manim import *
from manim.mobject.text.text_mobject import remove_invisible_chars


class IndividualProject(Scene):
    def PlayIntroduction(self):
        title_text = Text("Wagner-Fischer Algorithm")
        self.play(Write(title_text))
        self.play(title_text.animate.shift(UP*2))

        subtitle_name = Text("Riley Francis").scale(0.5)
        subtitle_netid = Text("rif17002").scale(0.5).shift(DOWN*0.5)
        self.play(FadeIn(subtitle_name, shift=UP), FadeIn(subtitle_netid, shift=UP))

        self.wait(2)

        self.play(FadeOut(subtitle_name, shift=DOWN), FadeOut(subtitle_netid, shift=DOWN))
        self.play(title_text.animate.scale(0.5).to_corner(UL))
        self.wait(1)

        return title_text


    def PlayIntroExample(self):
        typo_text = Tex("Get ready to ", "k", "earn!").scale(1.5)
        correct_text = Tex("Get ready to learn!").scale(1.5)
        self.play(Write(typo_text))
        self.wait(2)
        self.play(typo_text.animate.set_color_by_tex("k", RED))
        self.wait(2)

        ex1 = Tex("earn").align_to(typo_text, RIGHT).shift(DOWN)
        ex2 = Tex("learn").align_to(typo_text, RIGHT).shift(DOWN*1.5)
        ex3 = Tex("yearn").align_to(typo_text, RIGHT).shift(DOWN*2.2)

        self.play(FadeIn(ex1, ex2, ex3, shift=RIGHT))

        self.wait(2.5)
        self.play(ex1.animate.set_color(GRAY), ex3.animate.set_color(GRAY))
        self.wait(1)

        self.play(TransformMatchingShapes(typo_text, correct_text))
        self.wait(1)
        self.play(FadeOut(correct_text, ex1, ex2, ex3))


    def PlayManyWords(self, title_text):
        with open("a_words.text", "r") as word_file:
            words = word_file.readlines()

            grid = VGroup(*[Text(word).scale(0.6) for word in words]).arrange_in_grid(cols=5).to_edge(UP)

            self.play(FadeOut(title_text), FadeIn(grid))
            self.wait(1)
            self.play(grid.animate.to_edge(DOWN), run_time=7, rate_func=rate_functions.smoothererstep)

            self.wait(1)
            self.play(FadeOut(grid))

            word_count = Text("~171,000 Words").scale(1.5)
            self.play(Write(word_count), FadeIn(title_text))
            self.wait(6)
            self.play(FadeOut(word_count))


    def PlayPeopleInfo(self, title_text):
        wagnerImage = ImageMobject("Wagner.jpg").shift(LEFT*2).shift(DOWN*0.5).scale(2)
        fischerImage = ImageMobject("Fischer.jpg").shift(RIGHT*2).shift(DOWN*0.5).scale(2)

        wagnerText = Text("Robert Wagner").scale(0.6).move_to(wagnerImage.get_center()).align_to(wagnerImage, UP).shift(UP*0.75)
        fischerText = Text("Michael Fischer").scale(0.6).move_to(fischerImage.get_center()).align_to(fischerImage, UP).shift(UP*0.75)

        people = Group(wagnerImage, fischerImage, wagnerText, fischerText)

        self.play(title_text.animate.scale(1.75).center().to_edge(UP))

        self.play(FadeIn(people))
        self.wait(9)

        self.play(FadeOut(people), title_text.animate.scale(1/1.75).to_corner(UL))
        self.wait(1)
    

    def PlayDynamic(self):
        levenshtein = MathTex(r"\text{lev}(a,b)=\begin{cases}\text{len}(a) & \text{if } \text{len}(b)=0 \\ \text{len}(b) & \text{if } \text{len}(a)=0 \\ \text{lev}(\text{tail}(a),\text{tail}(b)) & \text{if } a[0]=b[0] \\ 1+\min\begin{cases}\text{lev}(\text{tail}(a),b) \\ \text{lev}(a,\text{tail}(b)) \\ \text{lev}(\text{tail}(a),\text{tail}(b))\end{cases} & \text{otherwise}\end{cases}")

        self.play(Write(levenshtein))
        self.wait(7)
        self.play(levenshtein.animate.shift(UP).scale(0.8))

        t_complexity = MathTex(r"O(3^n) \;\;\;\;\; n=\max(\text{len}(a), \text{len}(b))").shift(DOWN*2).set_color(TEAL_B)
        self.play(Write(t_complexity))
        self.wait(4)

        highlight = SurroundingRectangle(levenshtein[0][101:149], color=RED, fill_opacity=0.1)
        self.play(Create(highlight))
        self.wait(3)

        self.play(FadeOut(levenshtein, t_complexity, highlight))

        big_text = Text("Dynamic Programming").scale(1.5)
        self.play(Write(big_text))
        self.wait(4)
        self.play(FadeOut(big_text))
        

    
    def PlayOperations(self):
        self.wait(4.5)

        operate = MathTex(r"\text{heat}\rightarrow\text{heat}").shift(UP).scale(1.25)
        self.play(Write(operate))

        self.wait(6)

        operation_name = Tex("Insertion").scale(1.75).shift(UP*2.5)
        self.play(FadeIn(operation_name))

        toTransform = MathTex(r"\text{heat}\rightarrow\text{heat}", r"\text{s}").shift(UP).scale(1.25)
        toTransform[1][0].set_color(PURE_GREEN)
        self.play(TransformMatchingShapes(operate, toTransform))

        copy_1a = operation_name.copy()
        copy_1b = toTransform.copy()

        self.play(copy_1a.animate.scale(1/1.75).shift(DL*3.5), 
                  copy_1b.animate.scale(1/1.75).shift(DL*3.5).shift(UP*0.82))
        
        self.wait(1)

        #################
        o2_name = Tex("Deletion").scale(1.75).shift(UP*2.5)
        self.play(ReplacementTransform(operation_name, o2_name),
                  FadeOut(toTransform), FadeIn(operate))
        
        toTransform = MathTex(r"\text{heat}\rightarrow", r"\text{h}", r"\text{eat}").shift(UP).scale(1.25)
        toTransform[1][0].set_color(PURE_RED)
        self.play(TransformMatchingShapes(operate, toTransform))
        self.play(toTransform[1].animate.shift(DOWN*0.75), 
                  toTransform[2].animate.shift(LEFT*0.25))
        
        copy_2a = operation_name.copy()
        copy_2b = toTransform.copy()

        self.play(copy_2a.animate.scale(1/1.75).shift(DOWN*3.5), 
                  copy_2b.animate.scale(1/1.75).shift(DOWN*3.5).shift(UP))
        
        self.wait(1)

        ################
        o3_name = Tex("Substitution").scale(1.75).shift(UP*2.5)
        self.play(ReplacementTransform(o2_name, o3_name),
                  FadeOut(toTransform), FadeIn(operate))
        
        toTransform = MathTex(r"\text{heat}\rightarrow\text{hea}", r"\text{r}").shift(UP).scale(1.25)
        toTransform[1][0].set_color(BLUE_D)

        letter_t = operate[0][8].copy()
        self.play(letter_t.animate.shift(DOWN*0.75).set_color(GRAY))
        self.play(FadeOut(operate), FadeIn(toTransform))
        
        copy_3a = o3_name.copy()
        copy_3b = Group(toTransform.copy(), letter_t)

        self.play(copy_3a.animate.scale(1/1.75).shift(DR*3.5), 
                  copy_3b.animate.scale(1/1.75).shift(DR*3.5).shift(UP))
        
        self.wait(2)
        
        highlight = SurroundingRectangle(Group(copy_1a, copy_1b, copy_2a, copy_2b, copy_3a, copy_3b), fill_opacity=0.1, buff=MED_LARGE_BUFF)

        self.play(Write(highlight))

        self.wait(4)

        self.play(FadeOut(copy_1b, copy_2b, copy_3b, o3_name, toTransform, highlight),
                  copy_1a.animate.center().scale(0.8).to_edge(RIGHT).shift(UP*0.5),
                  copy_2a.animate.center().scale(0.8).to_edge(RIGHT),
                  copy_3a.animate.center().scale(0.8).to_edge(RIGHT).shift(DOWN*0.5))
        
        self.wait(1)

        operations = Group(copy_1a, copy_2a, copy_3a)
        return operations


    def _UpdateTableCell(self, table:Table, position:tuple, update_to:str, fill_time:int=0, prev_outlines:VGroup=None, table_elements:Group=None):
        col_label_cells = VGroup(*[table.get_cell((1, col)) for col in range(2, position[1]+2)])
        outline1 = SurroundingRectangle(col_label_cells, color=GREEN, buff=0, fill_opacity=0.2)
        row_label_cells = VGroup(*[table.get_cell((col, 1)) for col in range(2, position[0]+2)])
        outline2 = SurroundingRectangle(row_label_cells, color=GREEN, buff=0, fill_opacity=0.2)
        cell_to_update = table.get_cell((position[0]+1,position[1]+1))
        cellOutline = SurroundingRectangle(cell_to_update, color=YELLOW, buff=0, fill_opacity=0.1)
        
        outlines = VGroup(outline1, outline2, cellOutline)

        if prev_outlines is None:
            self.play(Create(outlines))
        else:
            self.play(ReplacementTransform(prev_outlines, outlines), run_time=0.25 if fill_time == 0 else 0.8)

        newT = Text(update_to).scale(0.75).move_to(cell_to_update.get_center())
        if table_elements is None:
            table_elements = VGroup(newT)
        else:
            table_elements.add(newT)

        if fill_time != 0:
            self.wait(fill_time)
        self.play(Write(newT), run_time=0.2 if fill_time == 0 else 0.8)

        return outlines, table_elements


    def PlayExample(self, operations:Group):
        self.wait(5)
        twoWords = MathTex(r"\text{b}", r"\text{i}", r"\text{g}", r"\text{g}", r"\text{e}", r"\text{r}", 
                           r"\rightarrow", r"\text{b}", r"\text{r}", r"\text{i}", r"\text{d}", r"\text{g}", r"\text{e}").scale(1.5)
        self.play(Write(twoWords))
        self.wait(2)
        self.play(FadeOut(twoWords))


        t = MathTex(r"\_", r"l").scale(1.5)
        t[1].set_color(BLACK)

        table = MobjectTable(
            table = [[Text("") for i in range(7)] for i in range(7)],
            row_labels=[t] + [twoWords[i] for i in range(6)],
            col_labels=[MathTex(r"\_").scale(1.5)] +[twoWords[i] for i in range(7,13)],
            include_outer_lines=True
        ).scale(0.6).to_corner(DL)

        self.play(table.create())

        self.wait(5)

        table_elements = Group()

        outline, table_elements = self._UpdateTableCell(table, (1,1), "0", 5, table_elements=table_elements)
        outline, table_elements = self._UpdateTableCell(table, (1,2), "1", 6, outline, table_elements=table_elements)
        outline, table_elements = self._UpdateTableCell(table, (1,3), "2", 6, outline, table_elements=table_elements)

        self.wait(1)

        for i in range(4,8):
            outline, table_elements = self._UpdateTableCell(table, (1,i), f"{i-1}", prev_outlines=outline, table_elements=table_elements)
        for i in range(2,8):
            outline, table_elements = self._UpdateTableCell(table, (i,1), f"{i-1}", prev_outlines=outline, table_elements=table_elements)

        self.wait(5)

        play_times = [15,9]
        for i in range(2):
            arrow1 = Arrow(table.get_cell((2,2+i)).get_center(), table.get_cell((3,3+i)).get_center()).set_color(RED)
            arrow2 = Arrow(table.get_cell((2,3+i)).get_center(), table.get_cell((3,3+i)).get_center()).set_color(RED)
            arrow3 = Arrow(table.get_cell((3,2+i)).get_center(), table.get_cell((3,3+i)).get_center()).set_color(RED)
            arrows = VGroup(arrow1, arrow2, arrow3)
            self.play(Create(arrows))

            outline, table_elements = self._UpdateTableCell(table, (2,2+i), str(i), play_times[i], outline, table_elements=table_elements)
            self.play(FadeOut(arrows))

        for i in range(4,8):
            outline, table_elements = self._UpdateTableCell(table, (2,i), f"{i-2}", prev_outlines=outline, table_elements=table_elements)

        toPut = [1,1,1,2,3,4, 2,2,2,2,2,3, 3,3,3,3,2,3, 4,4,4,4,3,2, 5,4,5,5,4,3]
        for row in range(5):
            for col in range(6):
                outline, table_elements = self._UpdateTableCell(table, (row+3, col+2), str(toPut[row*6 + col]), prev_outlines=outline, table_elements=table_elements)

        self.wait(0.5)
        self.play(FadeOut(outline))
        self.wait(1)
            
        self.play(operations[0].animate.scale(1.35).center().shift(RIGHT*4).shift(UP*1.5),
                  operations[1].animate.scale(1.35).center().shift(RIGHT*4),
                  operations[2].animate.scale(1.35).center().shift(RIGHT*4).shift(DOWN*1.5))
        
        self.play(operations.animate.shift(DOWN*0.75))
        
        toTransform = Text("bigger").scale(1.5).move_to(operations[0].get_center()).shift(UP*2)
        self.play(Write(toTransform))

        ins_arrow = Arrow(RIGHT*0.5, LEFT).set_color(RED).move_to(operations[0].get_center()).align_to(operations[0], RIGHT).shift(RIGHT*1.25)
        del_arrow = Arrow(DOWN*0.5, UP).set_color(RED).move_to(operations[1].get_center()).align_to(operations[1], RIGHT).shift(RIGHT*0.75)
        sub_arrow = Arrow(DR*0.5/(2**0.5), UL*0.75).set_color(RED).move_to(operations[2].get_center()).align_to(operations[2], RIGHT).shift(RIGHT)

        op_arrows = VGroup(ins_arrow, del_arrow, sub_arrow)
        self.play(Create(op_arrows))

        calc_outline = SurroundingRectangle(table.get_cell((8,8)), color=YELLOW, buff=0, fill_opacity=0.2)
        calc_outline_top = SurroundingRectangle(table.get_cell((1,8)), color=GREEN, buff=0, fill_opacity=0.2)
        calc_outline_left = SurroundingRectangle(table.get_cell((8,1)), color=GREEN, buff=0, fill_opacity=0.2)
        c_outlns = VGroup(calc_outline, calc_outline_left, calc_outline_top)
        self.play(Create(c_outlns))

        word_rect = SurroundingRectangle(toTransform[5], buff = 0.05, color=BLUE, fill_opacity=0.5, stroke_width=0)
        self.play(Create(word_rect))

        self.wait(18)
        pos, c_outlns, word_rect, word, goc = self._PerformOperation("del", table, (8,8), toTransform, 5, c_outlns, word_rect)
        self.wait(4)
        pos, c_outlns, word_rect, word, goc = self._PerformOperation(None, table, pos, word, 4, c_outlns, word_rect, grid_outlines=goc)
        self.wait(3)
        pos, c_outlns, word_rect, word, goc = self._PerformOperation(None, table, pos, word, 3, c_outlns, word_rect, grid_outlines=goc)
        self.wait(3)
        pos, c_outlns, word_rect, word, goc = self._PerformOperation("sub", table, pos, word, 2, c_outlns, word_rect, "d", grid_outlines=goc)
        self.wait(3)
        pos, c_outlns, word_rect, word, goc = self._PerformOperation(None, table, pos, word, 1, c_outlns, word_rect, grid_outlines=goc)
        self.wait(3)
        pos, c_outlns, word_rect, word, goc = self._PerformOperation("ins", table, pos, word, 0, c_outlns, word_rect, "r", grid_outlines=goc)
        self.wait(3)
        
        new_outline = c_outlns[0].copy()
        goc.add(new_outline)

        self.play(FadeOut(word_rect, c_outlns), new_outline.animate.set_color(GOLD))
        self.wait(4)
# 
        for item in goc:
            print(item)

        print(len(goc))

        # FadeOut(word, op_arrows, operations, table, table_elements, goc)
        self.play(FadeOut(word, op_arrows, operations, table, table_elements, goc))


    def _PerformOperation(self, op_type:str, table:Table, pos:tuple, word:Text, word_ind:int, outlines:VGroup, 
                          word_outline:SurroundingRectangle, to_insert:str=None, grid_outlines:VGroup=None):
        newWord = word
        
        
        if op_type == "ins":
            newPos = (pos[0], pos[1] - 1)
            newWord = Text(word.text[:word_ind+1] + to_insert + word.text[word_ind+1:]).move_to(word.get_center()).scale(1.5)
            word_rect = SurroundingRectangle(newWord[word_ind], buff = 0.05, color=BLUE, fill_opacity=0.5, stroke_width=0)
            anim = AnimationGroup(TransformMatchingShapes(word, newWord, shift=DOWN),
                                  ReplacementTransform(word_outline, word_rect))
        elif op_type == "del":
            newPos = (pos[0] - 1, pos[1])
            newWord = Text(word.text[:word_ind] + word.text[word_ind + 1:]).move_to(word.get_center()).scale(1.5)
            word_rect = SurroundingRectangle(newWord[word_ind - 1], buff = 0.05, color=BLUE, fill_opacity=0.5, stroke_width=0)
            anim = AnimationGroup(TransformMatchingShapes(word, newWord, shift=DOWN),
                                  ReplacementTransform(word_outline, word_rect))
        elif op_type == "sub":
            newPos = (pos[0] - 1, pos[1] - 1)
            newWord = Text(word.text[:word_ind] + to_insert + word.text[word_ind + 1:]).move_to(word.get_center()).scale(1.5)
            word_rect = SurroundingRectangle(newWord[word_ind - 1], buff = 0.05, color=BLUE, fill_opacity=0.5, stroke_width=0)
            anim = AnimationGroup(TransformMatchingShapes(word, newWord, shift=DOWN),
                                  ReplacementTransform(word_outline, word_rect))
        else:
            newPos = (pos[0] - 1, pos[1] - 1)
            word_rect = SurroundingRectangle(word[word_ind - 1], buff = 0.05, color=BLUE, fill_opacity=0.5, stroke_width=0)
            anim = AnimationGroup(ReplacementTransform(word_outline, word_rect))

        calc_outline = SurroundingRectangle(table.get_cell(newPos), color=YELLOW, buff=0, fill_opacity=0.2)
        calc_outline_top = SurroundingRectangle(table.get_cell((1,newPos[1])), color=GREEN, buff=0, fill_opacity=0.2)
        calc_outline_left = SurroundingRectangle(table.get_cell((newPos[0],1)), color=GREEN, buff=0, fill_opacity=0.2)
        c_outlns = VGroup(calc_outline, calc_outline_left, calc_outline_top) 

        grid_outline_copy = outlines[0].copy()
        if grid_outlines is None:
            grid_outlines = VGroup(grid_outline_copy)
        else:
            grid_outlines.add(grid_outline_copy)

        self.play(ReplacementTransform(outlines, c_outlns),
                  grid_outline_copy.animate.set_color(GOLD),
                  anim)
        return newPos, c_outlns, word_rect, newWord, grid_outlines


    def PlayCode(self):
        wf_code = Code("wf_algo.py", line_spacing=0.45)
        wf_code.code = remove_invisible_chars(wf_code.code)
        self.play(Write(wf_code))

        self.wait(1)
        code_line = SurroundingRectangle(wf_code.code[1], fill_opacity = 0.3, stroke_width = 0, fill_color = YELLOW, buff = 0.05).stretch_to_fit_width(wf_code.background_mobject.width).align_to(wf_code.background_mobject, LEFT)
        self.play(Create(code_line))
        self.wait(3)
        self.play(Transform(code_line, SurroundingRectangle(wf_code.code[3:6], fill_opacity = 0.3, stroke_width = 0, fill_color = YELLOW, buff = 0.05).stretch_to_fit_width(wf_code.background_mobject.width).align_to(wf_code.background_mobject, LEFT)))
        self.wait(7)
        self.play(Transform(code_line, SurroundingRectangle(wf_code.code[7], fill_opacity = 0.3, stroke_width = 0, fill_color = YELLOW, buff = 0.05).stretch_to_fit_width(wf_code.background_mobject.width).align_to(wf_code.background_mobject, LEFT)))
        self.wait(1)
        self.play(Transform(code_line, SurroundingRectangle(wf_code.code[8:11], fill_opacity = 0.3, stroke_width = 0, fill_color = YELLOW, buff = 0.05).stretch_to_fit_width(wf_code.background_mobject.width).align_to(wf_code.background_mobject, LEFT)))
        self.wait(4)
        self.play(Transform(code_line, SurroundingRectangle(wf_code.code[11:13], fill_opacity = 0.3, stroke_width = 0, fill_color = YELLOW, buff = 0.05).stretch_to_fit_width(wf_code.background_mobject.width).align_to(wf_code.background_mobject, LEFT)))
        self.wait(4)
        self.play(Transform(code_line, SurroundingRectangle(wf_code.code[13], fill_opacity = 0.3, stroke_width = 0, fill_color = YELLOW, buff = 0.05).stretch_to_fit_width(wf_code.background_mobject.width).align_to(wf_code.background_mobject, LEFT)))
        self.wait(2.5)
        self.play(Transform(code_line, SurroundingRectangle(wf_code.code[15], fill_opacity = 0.3, stroke_width = 0, fill_color = YELLOW, buff = 0.05).stretch_to_fit_width(wf_code.background_mobject.width).align_to(wf_code.background_mobject, LEFT)))
        self.wait(2)
        self.play(FadeOut(code_line, wf_code))

    
    def PlayTimeComplexity(self):
        t_complexity = MathTex(r"O(a\cdot b)").scale(1.5)
        self.play(Write(t_complexity))
        self.wait(10)
        self.play(Transform(t_complexity, MathTex(r"O(n\cdot a\cdot b)").scale(1.5)))
        self.wait(2)

        better_c = MathTex(r"O(n\cdot a\cdot b)", r"< O(3^{\max(a,b)})").scale(1.4)
        self.play(Transform(t_complexity, better_c, shift=LEFT))
        self.play(t_complexity[0].animate.set_color(GREEN))
        self.wait(2.5)
        self.play(FadeOut(t_complexity))

    
    def PlayNeuralNetwork(self):
        edges = []
        partitions = []
        c = 0
        layers = [3, 4, 5, 5, 5, 4, 3]

        for i in layers:
            partitions.append(list(range(c + 1, c + i + 1)))
            c += i
        for i, v in enumerate(layers[1:]):
                last = sum(layers[:i+1])
                for j in range(v):
                    for k in range(last - layers[i], last):
                        edges.append((k + 1, j + last + 1))

        vertices = np.arange(1, sum(layers) + 1)

        graph = Graph(
            vertices,
            edges,
            layout='partite',
            partitions=partitions,
            layout_scale=3.5,
            vertex_config={'radius': 0.20},
        )
        self.play(Write(graph))
        self.wait(4.5)
        self.play(FadeOut(graph))

    
    def PlayEnding(self):
        typo_text = Tex("I hope you ", "k", "earned something!").scale(1.5)
        correct_text = Tex("I hope you learned something!").scale(1.5)
        self.play(Write(typo_text))
        self.play(typo_text.animate.set_color_by_tex("k", RED))
        self.wait(0.5)

        self.play(TransformMatchingShapes(typo_text, correct_text))
        self.wait(1.75)
        self.play(FadeOut(correct_text))


##############################################################################################
    def construct(self):
        # config.max_files_cached = 255
        config.disable_caching = True
        title_text = self.PlayIntroduction()
        self.PlayIntroExample()
        self.PlayManyWords(title_text)
        self.PlayPeopleInfo(title_text)
        self.PlayDynamic()
        operations = self.PlayOperations()
        self.PlayExample(operations)
        self.PlayCode()
        self.PlayTimeComplexity()
        self.PlayNeuralNetwork()
        self.PlayEnding()
    

        self.wait(2)

        pass
