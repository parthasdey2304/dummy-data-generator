        let counter = 2;
        const add_columns = document.querySelector("#add_columns");
        add_columns.addEventListener('click', () => {
            const column_list_input = document.querySelector("#column_list_input");
            let st = column_list_input.innerHTML;
            st += `
                <div class="flex space-x-5">
                    <input type="text" placeholder="Column ${counter} name" class="w-1/2 border-2 border-black px-4 py-4 rounded-full font-semibold" id="columns_${counter}">
                    
                    <select name="" id="column_${counter}_data_type" class="w-1/2 border-2 border-black px-4 py-4 rounded-full font-semibold">
                        <option class="font-semibold" value="none">Select Data Type</option>
                        <option class="font-semibold" value="int">Random Integers</option>
                        <option class="font-semibold" value="decimal">Random Decimal</option>
                        <option class="font-semibold" value="text">AI text</option>
                        <option class="font-semibold" value="full_names">Full Names</option>
                    </select>
                </div> 
            `;
            counter++;
            column_list_input.innerHTML = st;
        });
