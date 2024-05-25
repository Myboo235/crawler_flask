<template>
    <div class="fixed w-full px-[1rem] top-10 xl:px-[30rem]" v-if="error_msg !== 'none'">
        <fwb-alert border type="danger" id="error_msg" closable class="px-4">
            {{ error_msg }}
        </fwb-alert>
    </div>
    <div class="fixed w-full px-[1rem] top-10 xl:px-[30rem]" v-if="info_msg !== 'none'">
        <fwb-alert border type="warning" closable>
            {{ info_msg }}
            <fwb-spinner />
        </fwb-alert>
    </div>
    <fwb-modal v-if="isShowModal" @close="closeModal">
        <template #header>
            <p v-if="typeAutoGenerate === 'crawl'">Auto generate text by crawl data 🌎</p>
            <p v-else>Auto generate text by model tranformers 🎰 </p>

        </template>
        <template #body>
            <div class="my-4">
                <p v-if="typeAutoGenerate === 'crawl'">This will create blog by by crawl data 🌎</p>
                <p v-else>This will create blog by by model tranformers 🎰 </p>
                <ul class="border-2 border-primary p-4 rounded-xl mt-4">
                    <li>
                        <div>
                            Speed
                        </div>
                        <div class="flex flex-col gap-2 bg-gray-300 p-2 rounded-xl">
                            <fwb-progress :progress="90" color="blue" label="crawl" />
                            <fwb-progress :progress="8" color="yellow" label="transforms model" class="text-white" />
                        </div>

                    </li>
                    <li>
                        <div>
                            Creative
                        </div>
                        <div class="flex flex-col gap-2 bg-gray-300 p-2 rounded-xl">
                            <fwb-progress :progress="10" color="blue" label="crawl" />
                            <fwb-progress :progress="90" color="yellow" label="transforms model" class="text-white" />
                        </div>
                    </li>
                </ul>

            </div>

            <label for="keyword" class="pb-4">Enter your keywork here</label>
            <textarea type="text" id="keyword"
                class="border border-gray-300 rounded-lg placeholder-[#4b3f2f] w-full p-5" placeholder="Your keyword"
                v-model="keyword" required />
        </template>
        <template #footer>
            <div class="flex justify-between">
                <fwb-button @click="closeModal" color="alternative">
                    Cancel
                </fwb-button>
                <fwb-button @click="autoGenerate()" class="bg-primary" id = "generate_data" >
                    Generate ✍️
                </fwb-button>
            </div>
        </template>
    </fwb-modal>
    <h2 class="text-white px-8 text-6xl font-bold lg:my-[4rem] cursor-pointer" v-if="props.type !== 'update'">Create Article.</h2>
    <h2 class="text-white px-8 text-6xl font-bold lg:my-[4rem] cursor-pointer" v-else>Update Article.</h2>
    <div class="my-[5rem] p-10 2xl:mx-[30rem] bg-tertiary rounded-2xl">
        <form class="mx-auto text-primary text-primary">
            <div class="mb-10 flex flex-col gap-2">
                <label for="title" class="mb-2 text-2xl">Title</label>
                <textarea type="text" id="title"
                    class="bg-secondary border border-gray-300 rounded-lg placeholder-[#4b3f2f] w-full p-5"
                    placeholder="Your title" v-model="title" required />
            </div>
            <div class="mb-5 flex flex-col gap-2">
                <label class="mb-2 text-2xl" for="image">Upload image</label>

                <textarea class="w-full rounded-lg cursor-pointer bg-secondary p-5 placeholder-[#4b3f2f]"
                    aria-describedby="image_blog" id="user_avatar" type="text" placeholder="Your image url or file path"
                    rows="10" v-model="imgs" />

                <div class="mt-1 text-sm text-gray-500 dark:text-gray-300" id="image_blog">A blog picture is useful to
                    attract viewer user, each url image split by a `enter`</div>
            </div>
            <div class="mb-5 flex flex-col gap-2">
                <label class="mb-2 text-2xl" for="content">Content</label>
                <textarea type="text" id="content"
                    class="rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full p-5 bg-secondary placeholder-[#4b3f2f]"
                    rows="20" placeholder="Your blog go here ..." v-model="content" />
            </div>
        </form>
        <div class="flex gap-4" v-if="props.type !== 'update'">
            <button
                id = "submit"
                class="text-secondary bg-primary border-secondary border-2 hover:text-primary hover:bg-secondary rounded-lg p-4 justify-self-end"
                @click="onSubmit()" :disabled="isDisable">
                Submit your blog 🚀
            </button>
            <button
                id = "crawl_submit"
                class="text-secondary bg-primary border-secondary border-2 hover:text-primary hover:bg-secondary rounded-lg p-4 justify-self-end"
                @click="showModal('crawl')" :disabled="isDisable">
                Auto generate text by crawl data 🌎
            </button>
            <button
                id = "gpt2_submit"
                class="text-secondary bg-primary border-secondary border-2 hover:text-primary hover:bg-secondary rounded-lg p-4 justify-self-end"
                @click="showModal('text')" :disabled="isDisable">
                Auto generate text using model ✨
            </button>

        </div>
        <button
            id = "update_submit"
            class="text-secondary bg-primary border-secondary border-2 hover:text-primary hover:bg-secondary rounded-lg p-4 justify-self-end"
            @click="onSubmit()" v-else>
            Update your blog 🚀
        </button>

    </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { FwbAlert, FwbSpinner, FwbButton, FwbModal, FwbProgress } from 'flowbite-vue'

const route = useRoute()
const router = useRouter()
const title = ref("")
const imgs = ref("")
const content = ref("")
const error_msg = ref("none")
const info_msg = ref("none")
const isShowModal = ref(false)
const keyword = ref("")
const typeAutoGenerate = ref("")
const isDisable = ref(false)
const streamInterval = 10;

const id = (route.params.id)
const props = defineProps(["type"])


if (props.type === "update") {
    axios.get(`http://localhost:5000/data/${id}`)
        .then(response => {
            const responseData = response.data;
            title.value = responseData.title;
            content.value = responseData.content.join("\n");
            imgs.value = responseData.img.join("\n");
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

function closeModal() {
    isShowModal.value = false
}
function showModal(type) {
    typeAutoGenerate.value = type
    isShowModal.value = true
}

const onSubmit = () => {
    error_msg.value = "none"
    if (title.value === "" || imgs.value === "" || content.value === "") {
        error_msg.value = "Please fill all the fields"

        return
    }

    if (props.type === "update") {
        axios.post('http://localhost:5000/update', {
            "_id": id,
            "title": title.value,
            "img": imgs.value.split("\n"),
            "content": content.value.split("\n")

        })
            .then(response => {
                router.push('/');
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                error_msg.value = error
            });
    } else {
        axios.post('http://localhost:5000/create', {
            "title": title.value,
            "img": imgs.value.split("\n"),
            "content": content.value.split("\n")

        })
            .then(response => {
                router.push('/');
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                error_msg.value = error
            });
    }

}

const autoGenerate = () => {

    closeModal()
    isDisable.value = true
    content.value = ""
    title.value = ""
    imgs.value = ""

    let content_generated_data = ""
    let title_generated_data = ""
    let imgs_generated_data = ""
    let content_generated_index = 0;
    let title_generated_index = 0;
    let imgs_generated_index = 0;


    info_msg.value = "Please wait. We are generate text for you..."
    axios.post(`http://localhost:5000/${typeAutoGenerate.value}_generate`, {
        "keyword": keyword.value
    }, {
        headers: {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
    })
        .then(response => {
            const responseData = response.data;
            content_generated_data = responseData.content_output
            title_generated_data = responseData.title_output
            imgs_generated_data = responseData.imgs.join("\n")
            info_msg.value = "none"
            const intervalId = setInterval(() => {
                if (content_generated_index < content_generated_data.length) {
                    content.value += content_generated_data[content_generated_index];
                    content_generated_index++;
                }
                if (title_generated_index < title_generated_data.length) {
                    title.value += title_generated_data[title_generated_index];
                    title_generated_index++;
                }
                if (imgs_generated_index < imgs_generated_data.length) {
                    imgs.value += imgs_generated_data[imgs_generated_index];
                    imgs_generated_index++;
                }
                if (
                    content_generated_index >= content_generated_data.length &&
                    title_generated_index >= title_generated_data.length &&
                    imgs_generated_index >= imgs_generated_data.length
                ) {
                    clearInterval(intervalId);
                    isDisable.value = false;
                }
            }, streamInterval);


        })
        .catch(error => {
            info_msg.value = "none"
            error_msg.value = error
            isDisable.value = false;
            console.error('Error fetching data:', error);
        });


}
</script>

<style lang="scss" scoped></style>